import os
import django
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "elastic_search.settings")
django.setup()

from store.models import Product

fake = Faker()

products = []

for _ in range(1000000):
    products.append(
        Product(
            title=fake.word(),
            description=fake.text(),
            price=fake.random_int(min=1000, max=1000000),
            is_active=fake.boolean()
        )
    )

Product.objects.bulk_create(products, batch_size=1000)

print("Products created")
