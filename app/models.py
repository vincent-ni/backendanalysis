from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
	isbn = models.CharField(max_length=13, primary_key=True)
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	pub_house = models.CharField(max_length=200)

	def book_list(self):
		return self.stats_set.all()

	def __str__(self):
		return self.title

class Stats(models.Model):
	book = models.ForeignKey(Book)
	longitude = models.CharField(max_length=200)
	latitude = models.CharField(max_length=200)
	locality = models.CharField(max_length=200)

	def __str__(self):
		return self.book
