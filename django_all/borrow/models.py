from django.db import models
from booktype.models import Book 
from members.models import Members, Point
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
status = (
		("ຢືມປື້ມ", "ຢືມປື້ມ"),
		("ຄືນປື້ມ", "ຄືນປື້ມ"),
	)




class BorrowBook(models.Model):
	books = models.ManyToManyField(Book)

	def __str__(self):
		return f'{self.id}'

	class Meta:
		ordering = ['id']



class CheckOutBorrow(models.Model):
	book = models.OneToOneField(BorrowBook, on_delete=models.CASCADE)
	point = models.ForeignKey(Point, on_delete=models.CASCADE)
	employee = models.ForeignKey(User, on_delete=models.CASCADE)
	date_rent = models.DateTimeField(default=timezone.now)
	date_return = models.DateField(max_length=8, help_text='YY-MM-DD')
	status = models.CharField(max_length=7, choices=status, default="ຢືມປື້ມ")


	def __str__(self):
		return f'{self.id}'

	class Meta:
		ordering = ['id']



class ReclaimBook(models.Model):
	borrow = models.OneToOneField(CheckOutBorrow, on_delete=models.CASCADE)
	date_reclaim = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.id}'



class BookReturn(models.Model):
	borrow = models.OneToOneField(CheckOutBorrow, on_delete=models.CASCADE)
	employee = models.ForeignKey(User, on_delete=models.CASCADE)
	return_book = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.id}'






