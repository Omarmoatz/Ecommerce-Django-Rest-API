import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

django.setup()


from  random import randint
from faker import Faker
from product.models import Product

def create_product(n):
    faker = Faker()
    ctg = ['Labtobs','Food','Toys','Phones']
    for _ in range(n):
        Product.objects.create(
            name = faker.name(),
            description= faker.text(max_nb_chars=500),
            price = randint(0,1000),
            category = ctg[randint(0,3)],
            brand = faker.name(),
            quantity = randint(0,10),
        )
    print(f'{n} product created')

create_product(5)
