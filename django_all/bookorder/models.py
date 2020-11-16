from django.db import models
from django.contrib.auth.models import User
from booktype.models import BookStore

# Create your models here.

class BookOrder(models.Model):
	date_order = models.DateField(max_length=8, help_text='YY-MM-DD')
	amount = models.CharField(max_length=4)
	bookstore = models.ForeignKey(BookStore, on_delete=models.CASCADE)
	employee = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

	def __str__(self):
		return f'ID: {self.id}'

	class Meta:
		ordering = ['-id']

