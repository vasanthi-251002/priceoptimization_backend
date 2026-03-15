from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Product, Category
from .serializers import ProductSerializer, ProductListSerializer, CategorySerializer
from .filters import ProductFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    """
    Full CRUD for products.
    - list   : GET  /api/products/
    - create : POST /api/products/
    - retrieve: GET /api/products/<id>/
    - update : PUT  /api/products/<id>/
    - partial_update: PATCH /api/products/<id>/
    - destroy: DELETE /api/products/<id>/
    - demand_forecast: GET /api/products/demand-forecast/
    - pricing_optimization: GET /api/products/pricing-optimization/
    """
    queryset = Product.objects.select_related('category').all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['name', 'selling_price', 'cost_price', 'units_sold', 'created_at']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductSerializer

    @action(detail=False, methods=['get'], url_path='demand-forecast')
    def demand_forecast(self, request):
        """
        Returns products with demand forecast data and chart-ready series.
        Query param: ?category=Electronics
        """
        qs = self.filter_queryset(self.get_queryset())
        products = ProductListSerializer(qs, many=True).data

        # Build chart data: demand_forecast vs selling_price per product
        chart_data = {
            'labels': [p['name'] for p in products],
            'demand_forecast': [p['demand_forecast'] for p in products],
            'selling_price': [float(p['selling_price']) for p in products],
            'units_sold': [p['units_sold'] for p in products],
        }

        return Response({
            'products': products,
            'chart_data': chart_data,
        })

    @action(detail=False, methods=['get'], url_path='pricing-optimization')
    def pricing_optimization(self, request):
        """
        Returns products with their optimized prices.
        """
        qs = self.filter_queryset(self.get_queryset())
        products = ProductSerializer(qs, many=True).data
        return Response({'products': products})

    @action(detail=False, methods=['get'], url_path='stats')
    def stats(self, request):
        """Dashboard summary stats."""
        from django.db.models import Sum, Avg, Count
        qs = Product.objects.all()
        data = qs.aggregate(
            total_products=Count('id'),
            total_stock=Sum('stock_available'),
            total_units_sold=Sum('units_sold'),
            avg_rating=Avg('customer_rating'),
        )
        return Response(data)
