import csv
import os
from django.core.management.base import BaseCommand
from products.models import Product, Category
from authentication.models import User


PRODUCTS = [
    {"product_id": 1, "name": "Eco-Friendly Water Bottle", "description": "A sustainable, reusable water bottle made from recycled materials.", "cost_price": 5.0, "selling_price": 12.99, "category": "Outdoor & Sports", "stock_available": 500, "units_sold": 200, "customer_rating": 4, "demand_forecast": 250, "optimized_price": 11.5},
    {"product_id": 2, "name": "Wireless Earbuds", "description": "Bluetooth 5.0 wireless earbuds with noise cancellation and long battery life.", "cost_price": 25.0, "selling_price": 59.99, "category": "Electronics", "stock_available": 300, "units_sold": 150, "customer_rating": 5, "demand_forecast": 180, "optimized_price": 55.0},
    {"product_id": 3, "name": "Organic Cotton T-Shirt", "description": "Soft, breathable t-shirt made from 100% organic cotton.", "cost_price": 8.0, "selling_price": 19.99, "category": "Apparel", "stock_available": 400, "units_sold": 100, "customer_rating": 4, "demand_forecast": 120, "optimized_price": 18.5},
    {"product_id": 4, "name": "Smart Home Hub", "description": "Control all your smart home devices with this central hub.", "cost_price": 40.0, "selling_price": 99.99, "category": "Home Automation", "stock_available": 150, "units_sold": 75, "customer_rating": 4, "demand_forecast": 90, "optimized_price": 95.0},
    {"product_id": 5, "name": "Electric Scooter", "description": "Lightweight electric scooter with a range of 20 miles.", "cost_price": 150.0, "selling_price": 299.99, "category": "Transportation", "stock_available": 80, "units_sold": 40, "customer_rating": 5, "demand_forecast": 50, "optimized_price": 285.0},
    {"product_id": 6, "name": "Noise-Canceling Headphones", "description": "Over-ear headphones with active noise cancellation.", "cost_price": 50.0, "selling_price": 129.99, "category": "Electronics", "stock_available": 200, "units_sold": 90, "customer_rating": 4, "demand_forecast": 110, "optimized_price": 125.0},
    {"product_id": 7, "name": "Smartwatch", "description": "Feature-packed smartwatch with heart rate monitor and GPS.", "cost_price": 70.0, "selling_price": 149.99, "category": "Wearables", "stock_available": 250, "units_sold": 130, "customer_rating": 5, "demand_forecast": 160, "optimized_price": 145.0},
    {"product_id": 8, "name": "Portable Solar Charger", "description": "Compact solar charger for outdoor use.", "cost_price": 20.0, "selling_price": 39.99, "category": "Outdoor & Sports", "stock_available": 300, "units_sold": 140, "customer_rating": 4, "demand_forecast": 170, "optimized_price": 38.0},
    {"product_id": 9, "name": "Fitness Tracker", "description": "Wearable fitness tracker with sleep monitoring.", "cost_price": 30.0, "selling_price": 59.99, "category": "Wearables", "stock_available": 350, "units_sold": 180, "customer_rating": 4, "demand_forecast": 200, "optimized_price": 57.0},
    {"product_id": 10, "name": "Bluetooth Speaker", "description": "Portable Bluetooth speaker with excellent sound quality.", "cost_price": 15.0, "selling_price": 45.99, "category": "Electronics", "stock_available": 400, "units_sold": 210, "customer_rating": 4, "demand_forecast": 240, "optimized_price": 43.0},
]


class Command(BaseCommand):
    help = 'Seed the database with sample products and a demo admin user'

    def handle(self, *args, **kwargs):
        # Create admin user
        if not User.objects.filter(email='admin@demo.com').exists():
            User.objects.create_superuser(
                email='admin@demo.com',
                password='Admin@1234',
                first_name='Amish',
                last_name='Singh',
            )
            self.stdout.write(self.style.SUCCESS('Admin user created: admin@demo.com / Admin@1234'))

        # Seed products
        for item in PRODUCTS:
            cat, _ = Category.objects.get_or_create(name=item['category'])
            Product.objects.update_or_create(
                name=item['name'],
                defaults={
                    'description': item['description'],
                    'cost_price': item['cost_price'],
                    'selling_price': item['selling_price'],
                    'category': cat,
                    'stock_available': item['stock_available'],
                    'units_sold': item['units_sold'],
                    'customer_rating': item['customer_rating'],
                    'demand_forecast': item['demand_forecast'],
                    'optimized_price': item['optimized_price'],
                }
            )
        self.stdout.write(self.style.SUCCESS(f'Seeded {len(PRODUCTS)} products successfully.'))
