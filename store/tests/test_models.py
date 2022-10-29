from django.test import TestCase
from store.models import Category, Producer, Product


class TestCategoryModel(TestCase):

    def setUp(self) -> None:
        self.data1 = Category.objects.create(name='testowa', slug='testowa')

    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_name(self):
        data = self.data1
        self.assertEqual(str(data), 'testowa')

class TestProducerModel(TestCase):

    def setUp(self) -> None:
        self.data1 = Producer.objects.create(name='kiedrowski', slug='kiedrowski')

    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Producer))

    def test_category_model_name(self):
        data = self.data1
        self.assertEqual(str(data), 'kiedrowski')


class TestProductModel(TestCase):

    def setUp(self) -> None:
        Category.objects.create(name='testowa', slug='testowa')
        Producer.objects.create(name='kiedrowski', slug='kiedrowski')
        self.data1 = Product.objects.create(category_id=1, producer_id=1, name='chleb pszenny',
                                            slug='chleb-pszenny', price='10', image='chleb')

    def test_product_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'chleb pszenny')