from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), allow_null=True)
    profit_margin = serializers.ReadOnlyField()
    margin_percentage = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'cost_price', 'selling_price',
            'category', 'category_name', 'stock_available', 'units_sold',
            'customer_rating', 'demand_forecast', 'optimized_price',
            'profit_margin', 'margin_percentage', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        cost = data.get('cost_price', getattr(self.instance, 'cost_price', None))
        selling = data.get('selling_price', getattr(self.instance, 'selling_price', None))
        if cost and selling and selling < cost:
            raise serializers.ValidationError({'selling_price': 'Selling price must be >= cost price.'})
        return data


class ProductListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for list views."""
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'category', 'category_name', 'cost_price',
            'selling_price', 'stock_available', 'units_sold',
            'demand_forecast', 'optimized_price', 'customer_rating'
        ]
