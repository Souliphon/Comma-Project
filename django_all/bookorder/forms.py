from django.forms import ModelForm
from .models import BookOrder


class BookOrderForm(ModelForm):
	class Meta:
		model = BookOrder
		fields = [
			'date_order',
			'amount',
			'bookstore'
		]

		labels = {
			'date_order': 'ວັນເດືອນປີສັ່ງຊື້ປື້ມ',
			'amount': 'ຈຳນວນ',
			'bookstore': 'ຮ້ານຂາຍປື້ມ',
		}