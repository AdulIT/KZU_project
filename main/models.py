from django.conf import settings
from django.db import models
from django.utils import timezone

#Menu
#News
#List of University
#Categories of university
#About universities
#Profession

class News(models.Model):
	title = models.CharField('Заголовок новости', max_length=200, null=True)
	textOfNews = models.TextField(null=True)
	dateOfPublished = models.DateTimeField(default=timezone.now)

	class Meta:
		verbose_name = 'Новости'
		verbose_name_plural = 'Новости'

	def __str__(self):
		return '%s, %s' % (self.title, self.textOfNews)

class City(models.Model):
	# ASTANA = 'Ast'
	# ALMATY = 'Ala'
	# CITY_CHOICES = (
	# 	(ASTANA, 'Astana'),
	# 	(ALMATY, 'Almaty'),
	# 	)
	# city_choices = models.CharField(max_length=100,
	# 	choices=CITY_CHOICES,
	# 	default=ASTANA)
	name_of_city = models.CharField(max_length=100, null=True, blank=True)


	def __str__(self):
		return self.name_of_city

	class Meta:
		verbose_name = 'Город'
		verbose_name_plural = 'Городa'


class University(models.Model):
	name = models.CharField(max_length=250, null=True)
	city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
	place_in_the_rating = models.IntegerField()


	def __str__(self):
		return '%s %s'%(self.name, self.place_in_the_rating)


	class Meta:
		verbose_name = 'Университет'
		verbose_name_plural = 'Университеты'


class Faculty(models.Model):
	faculty_name = models.CharField(max_length=100)
	abbr = models.CharField(max_length=50)
	profession = models.ForeignKey('Profession', on_delete=models.SET_NULL, null=True)


class Profession(models.Model):
	profession_name = models.CharField('Computer Science, IT, management, etc.', max_length=100, null=True)

	def __str__(self):
		return self.profession_name


class Carousel(models.Model):
	title = models.CharField(max_length=100, null=True)
	caption = models.TextField(null=True)


class Slider(models.Model):
	# image = models.ImageField(upload_to='images', height_field=900, width_field=400)
	# carousel = models.ForeignKey(models.Carousel)
	pass


class Compare(models.Model):
	pass