from django.db import models
from django.urls import reverse
from phone_field import PhoneField
from django.utils import timezone

# Create your models here.


book_status = (
		("ວ່າງ", "ວ່າງ"),
		("ຖືກຢືມ", "ຖຶກຢືມ"),
	)




class BookType(models.Model):
	name = models.CharField(max_length=20, unique=True)
	zone_number = models.CharField(max_length=1, unique=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('booktype-detail', kwargs={'pk': self.pk})

	class Meta:
		ordering = ['-id']



class BookStore(models.Model):
	name = models.CharField(max_length=20)
	tel = PhoneField(blank=True, help_text='Contact phone number e.g 0255667788-856', unique=True)
	email = models.EmailField(max_length=30)
	village = models.CharField(max_length=20)
	district = models.CharField(max_length=20)
	province = models.CharField(max_length=20)

	def __str__(self):
		return self.name


	def get_absolute_url(self):
		return reverse('bookstore-detail', kwargs={'pk': self.pk})

	class Meta:
		ordering = ['-id']




class Book(models.Model):
	title = models.CharField(max_length=50)
	subject_heading = models.CharField(max_length=50)
	primary_author = models.CharField(max_length=20)
	coauthor = models.CharField(max_length=20, null=True, blank=True)
	original_language = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	page_element = models.CharField(max_length=4)
	ISBN = models.CharField(max_length=20)
	status = models.CharField(max_length=12, choices=book_status, default="ວ່າງ")
	date_created = models.DateTimeField(default=timezone.now)
	booktype = models.ForeignKey(BookType, on_delete=models.CASCADE)
	# bookstore = models.ForeignKey(BookStore, on_delete=models.CASCADE)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('book-detail', kwargs={'pk': self.pk})

	class Meta:
		ordering = ['-id']











