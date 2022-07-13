from datetime import timezone
from django.test import TestCase

from base.models import Product


class ProductTest(TestCase):
    def create_product(self, title="only a test", body="yes, this only a test"):
        return Product.objects.create(title=title, body=body, created_at=timezone)

    def test_whatever_creation(self):
        # w = self.create_product()
        # self.assertTrue(isinstance(w, Product))
        # self.assertEqual(w.__unicode__(), w.title)
        pass

    # def test_whatever(self):
    # self.assertTrue(True == True)
