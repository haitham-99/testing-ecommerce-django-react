import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from rest_framework.response import Response
from base.models import Product, Review
from base.serializers import ProductSerializer
# from django.contrib.auth.models import User
from rest_framework.authtoken.admin import User


@pytest.mark.django_db
def test_product_creation(create_product):
    p = create_product
    assert isinstance(p, Product) is True
    assert p.name == "my product"


@pytest.mark.django_db
def test_product_info(create_product):
    p = create_product
    assert p.name == "my product"
    assert p.price == 1000
    assert p.brand == "my brand"
    assert p.countInStock == 3
    assert p.category == "Sample category"
    assert p.description == "new product"


def test_update_product(create_product):
    Product.name = "my new name"
    assert Product.name == "my new name"


def test_delete_product(create_product):
    Product.delete(create_product)
    count = Product.objects.all().count()
    assert count == 0
