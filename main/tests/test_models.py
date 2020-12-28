from django.test import TestCase
from main.models import News, City, University, Faculty, Profession, Carousel

class NewsTestModels(TestCase):

	def setUp(self):
		News.objects.create(
			title='The most popular profession',
			textOfNews='It is a description of the news')

	def test_title_label(self):
		news = News.objects.get(id=1)
		field_label = news._meta.get_field('title').verbose_name
		self.assertEquals(field_label, 'Заголовок новости')

	def test_title_label(self):
		news = News.objects.get(id=1)
		field_label = news._meta.get_field('textOfNews').verbose_name
		self.assertEquals(field_label, 'textOfNews')

	def test_title_max_length(self):
		news = News.objects.get(id=1)
		max_length = news._meta.get_field('title').max_length
		self.assertEquals(max_length, 200)


class CityTestModels(TestCase):

	def setUp(self):
		City.objects.create(
			name_of_city='Astana')

	def test_name_of_city_label(self):
		city = City.objects.get(id=1)
		field_label = city._meta.get_field('name_of_city').verbose_name
		self.assertEquals(field_label, 'name of city')

	def test_city_max_length(self):
		city = City.objects.get(id=1)
		max_length = city._meta.get_field('name_of_city').max_length
		self.assertEquals(max_length, 100)