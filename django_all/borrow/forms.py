from django.forms import ModelForm
from .models import CheckOutBorrow, BorrowBook, ReclaimBook, BookReturn

class CheckOutBorrowForm(ModelForm):
	class Meta:
		model = CheckOutBorrow
		fields = [
			'book',
			'point',
			'status',
			'date_return'
		]

		labels = {
			'book': 'ລະຫັດລາຍລະອຽດປື້ມ',
			'point': 'ລະຫັດການຊື້ຈຳນວນສິນຄ້າ',
			'status': 'ສະຖານະການຢືມປື້ມ',
			'date_return': 'ວັນເດືອນປີຄືນປື້ມ',
		}



class BorrowUpdateForm(ModelForm):
	class Meta:
		model = CheckOutBorrow
		fields = [
			# 'book',
			# 'point',
			'status',
			'date_return'
		]

		labels = {
			# 'book': 'ລະຫັດລາຍລະອຽດປື້ມ',
			# 'point': 'ລະຫັດການຊື້ຈຳນວນສິນຄ້າ',
			'status': 'ສະຖານະການຢືມປື້ມ',
			'date_return': 'ວັນເດືອນປີຄືນປື້ມ',
		}



class ReuturnBorrowUpdateForm(ModelForm):
	class Meta:
		model = CheckOutBorrow
		fields = [
			# 'book',
			# 'point',
			'status',
			# 'date_return'
		]

		labels = {
			# 'book': 'ລະຫັດລາຍລະອຽດປື້ມ',
			# 'point': 'ລະຫັດການຊື້ຈຳນວນສິນຄ້າ',
			'status': 'ສະຖານະການຢືມປື້ມ',
			# 'date_return': 'ວັນເດືອນປີຄືນປື້ມ',
		}



class ReclaimBookForm(ModelForm):
	class Meta:
		model = ReclaimBook
		fields = [
			'borrow'
		]

		labels = {
			'borrow': 'ລະຫັດການຢືມປື້ມ'
		}



class BookReturnForm(ModelForm):
	class Meta:
		model = BookReturn
		fields = [
			'borrow'
		]

		labels = {
			'borrow': 'ລະຫັດການຢືມປື້ມ'
		}



# class BookReturnTwoForm(ModelForm):
# 	class Meta:
# 		model = BookReturn
# 		fields = [
# 			'borrow',
# 			'return_book'
# 		]

# 		labels = {
# 			'borrow': 'ລະຫັດການຢືມປື້ມ',
# 			'return_book': 'ວັນເດືອນປີທີ່ໄດ້ຮັບປື້ມ'

# 		}














