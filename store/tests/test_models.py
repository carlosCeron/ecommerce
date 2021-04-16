from django.test import TestCase
from store.models import Category, Product


class TestCategoriesModel(TestCase):
	
	def setUp(self) -> None:
		self.data1 = Category.objects.create(name='django', slug='django')
	
	def test_category_model_entry(self):
		"""
		Test category models entry, data insertion/types/field attributes
		"""
		data = self.data1
		self.assertTrue(isinstance(data, Category))
	
	def test_category_model_name(self):
		"""
		Test category model return the model name
		"""
		data = self.data1
		self.assertEqual(str(data), "django")
