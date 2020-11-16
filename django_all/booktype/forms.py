from django.forms import ModelForm
from .models import BookType, Book, BookStore
from django import forms



class BookTypeForm(ModelForm):
	class Meta:
		model = BookType
		fields = ['name', 'zone_number']
		labels = {
			'name': 'ຊື່ປະເພດປື້ມ',
			'zone_number': 'ເລກໝວດເອກະສານ',
		}


class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = [
			'title',
			'subject_heading',
			'primary_author',
			'coauthor',
			'original_language',
			'price',
			'page_element',
			'ISBN',
			'status',
			'booktype',
			# 'bookstore'
		]
		labels = {
			'title': 'ຊື່ເລື່ອງ',
			'subject_heading': 'ຫົວເລື່ອງ',
			'primary_author': 'ຜູ້ແຕ່ງຫຼັກ',
			'coauthor': 'ຜູ້ແຕ່ງທ່ານອື່ນ',
			'original_language': 'ພາສາຕົ້ນສະບັບ',
			'price': 'ລາຄາ',
			'page_element': 'ຈຳນວນໜ້າ',
			'ISBN': 'ລະຫັດກຳກັບປື້ມ',
			'status': 'ສະຖານະປື້ມ',
			'booktype': 'ປະເພດປື້ມ',
			# 'bookstore': 'ຮ້ານຂາຍປື້ມ'
		}

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'subject_heading': forms.TextInput(attrs={'class': 'form-control'}),
			'primary_author': forms.TextInput(attrs={'class': 'form-control'}),
			'coauthor': forms.TextInput(attrs={'class': 'form-control'}),
			'original_language': forms.TextInput(attrs={'class': 'form-control'}),
			'price': forms.TextInput(attrs={'class': 'form-control'}),
			'page_element': forms.TextInput(attrs={'class': 'form-control'}),
			'ISBN': forms.TextInput(attrs={'class': 'form-control'}),
			'status': forms.Select(attrs={'class': 'form-control'}),
			'booktype': forms.Select(attrs={'class': 'form-control'}),
			'bookstore': forms.Select(attrs={'class': 'form-control'}),

		}



class BookUpdateBorrowForm(ModelForm):
	class Meta:
		model = Book
		fields = [
			'status'
		]
		labels = {
			'status': 'ສະຖານະປື້ມ',
		}



class BookStoreForm(ModelForm):
	class Meta:
		model = BookStore
		fields = [
			'name',
			'tel',
			'email',
			'village',
			'district',
			'province'
		]
		labels = {
			'name': 'ຊື່ຮ້ານຂາຍປື້ມ',
			'tel': 'ເບີໂທ',
			'email': 'ອີເມວ',
			'village': 'ບ້ານ',
			'district': 'ເມືອງ',
			'province': 'ແຂວງ',
		}



