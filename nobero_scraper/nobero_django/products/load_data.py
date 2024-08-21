import json
from products.models import Product

def load_data_from_json():
    with open('data.json', 'r') as file:
        data = json.load(file)
        for item in data:
            Product.objects.create(
                title=item['title'],
                price=item['price'],
                mrp=item.get('mrp'),
                last_7_day_sale=item.get('last_7_day_sale'),
                fit=item.get('fit'),
                fabric=item.get('fabric'),
                neck=item.get('neck'),
                sleeve=item.get('sleeve'),
                pattern=item.get('pattern'),
                length=item.get('length'),
                description=item.get('description')
            )
