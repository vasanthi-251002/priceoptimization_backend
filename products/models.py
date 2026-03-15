from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True, default='')
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    stock_available = models.PositiveIntegerField(default=0)
    units_sold = models.PositiveIntegerField(default=0)
    customer_rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    demand_forecast = models.PositiveIntegerField(default=0)
    optimized_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['category']),
        ]

    def __str__(self):
        return self.name

    @property
    def profit_margin(self):
        if self.selling_price and self.cost_price:
            return round(float(self.selling_price - self.cost_price), 2)
        return 0.0

    @property
    def margin_percentage(self):
        if self.selling_price and float(self.selling_price) > 0:
            return round((float(self.selling_price - self.cost_price) / float(self.selling_price)) * 100, 1)
        return 0.0
