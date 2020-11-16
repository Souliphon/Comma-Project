from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.urls import reverse
from booktype.models import Book
from members.models import Point
from django.contrib.auth.models import User
from .models import BorrowBook, CheckOutBorrow, ReclaimBook, BookReturn
from .forms import CheckOutBorrowForm, BorrowUpdateForm, ReclaimBookForm, BookReturnForm, ReuturnBorrowUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import get_template
from django.views import View
import xhtml2pdf.pisa as pisa 
from io import BytesIO
from django.utils import timezone
from django.http import HttpResponse
from datetime import date 
import csv




# Create your views here.
@login_required
def export_borrow_book(request):
	response = HttpResponse(content_type='text/csv')
	response.write(u'\ufeff'.encode('utf-8'))
	writer = csv.writer(response)
	writer.writerow(['ລະຫັດການຢືມປື້ມ', 'ລະຫັດລາຍລະອຽດປື້ມ', 'ລະຫັດສະຖິຕິການຊື້ຈຳນວນສິນຄ້າ', 'ພະນັກງານ', 'ວັນເດືອນປີຢຶມປື້ມ', 'ວັນເດືອນປີຄືນປື້ມ' ])

	for borrow in CheckOutBorrow.objects.all().values_list('id', 'book', 'point', 'employee', 'date_rent', 'date_return'):
		writer.writerow(borrow)

	response['Content-Disposition'] = 'attachment; filename="book_borrow.csv"'

	return response



@login_required
def export_reclaim_book(request):
	response = HttpResponse(content_type='text/csv')
	response.write(u'\ufeff'.encode('utf-8'))
	writer = csv.writer(response)
	writer.writerow(['ລະຫັດການທວງປື້ມ', 'ລະຫັດການຢືມປື້ມ','ວັນເດືອນປິທວງປື້ມ' ])

	for borrow in ReclaimBook.objects.all().values_list('id', 'borrow','date_reclaim'):
		writer.writerow(borrow)

	response['Content-Disposition'] = 'attachment; filename="reclaim_book.csv"'

	return response



@login_required
def export_book_return(request):
	response = HttpResponse(content_type='text/csv')
	response.write(u'\ufeff'.encode('utf-8'))
	writer = csv.writer(response)
	writer.writerow(['ລະຫັດການຮັບເອົາປື້ມ', 'ລະຫັດການຢືມປື້ມ', 'ພະນັກງານ', 'ວັນເດືອນປີຮັບເອົາປື້ມ' ])

	for borrow in BookReturn.objects.all().values_list('id', 'borrow','employee', 'return_book'):
		writer.writerow(borrow)

	response['Content-Disposition'] = 'attachment; filename="book_return.csv"'

	return response  



# class Render:

# 	@staticmethod
# 	def render(path: str, params: dict):
# 		template = get_template(path)
# 		html = template.render(params)
# 		response = BytesIO()
# 		pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
# 		if not pdf.err:
# 			return HttpResponse(response.getvalue(), content_type='application/pdf')
# 		else:
# 			return HttpResponse("Error Rendering PDF", status=400)


# class BillPDFView(LoginRequiredMixin, View):
# 	def get(self, request, pk, *args, **kwargs):
# 		borrow = CheckOutBorrow.objects.get(id=pk)
# 		today = timezone.now()
# 		params = {
# 			'today': today,
# 			'borrow': borrow,
# 			'request': request
# 		}

# 		return Render.render('borrow/bill_pdf_template.html', params)



def borrow_book_list(request):
	try:
		the_id = request.session['borrow_id']
	except:
		the_id = None
	if the_id:
		borrow_book = BorrowBook.objects.get(id=the_id)
		context = {'borrow_book': borrow_book}
	else:
		empty_message = "ການຢືມປື້ມຂອງທ່ານວ່າງເປົ່າ, ກະລຸນາເລືອກຕັດຄະແນນເພື່ອຢືມປື້ມ"
		context = {'empty': True, "empty_message": empty_message}

	template = 'borrow/borrow_book_list.html'
	return render(request, template, context)


def borrow_book_update(request, pk):
	request.session.set_expiry(1200)

	try:
		the_id = request.session['borrow_id']
	except:
		new_borrow = BorrowBook()
		new_borrow.save()
		request.session['borrow_id'] = new_borrow.id 
		the_id = new_borrow.id 

	borrow_book = BorrowBook.objects.get(id=the_id)

	try:
		book = Book.objects.get(id=pk)
	except Book.DoesNotExist:
		pass
	except:
		pass

	if not book in borrow_book.books.all():
		borrow_book.books.add(book)
	else:
		borrow_book.books.remove(book)

	request.session['items_total'] = borrow_book.books.count()

	return HttpResponseRedirect(reverse('borrow-book-list'))


@login_required
def check_out_borrow_create(request):
	
	if request.method == 'POST':
		form = CheckOutBorrowForm(request.POST)
		if form.is_valid():

			instance = form.save(commit=False)
			instance.employee = request.user
			# borrow = CheckOutBorrow.objects.get(id=pk)
			
			instance.save()
			del request.session['borrow_id']
			del request.session['items_total']
			return redirect('check-out-borrow-list')
	else:

		form = CheckOutBorrowForm()
	return render(request, 'borrow/check_out_borrow_create.html', {'form': form})




@login_required
def check_out_borrow_update(request, pk):
	order = CheckOutBorrow.objects.get(id=pk)
	form = CheckOutBorrowForm(instance=order)

	if request.method == 'POST':
		form = CheckOutBorrowForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('check-out-borrow-list')

	else:

		form = CheckOutBorrowForm(instance=order)
	return render(request, 'borrow/check_out_borrow_create.html', {'form': form})



@login_required
def check_out_borrow_list(request):
	borrow = CheckOutBorrow.objects.all()
	context = {
		'borrow': borrow
	}
	return render(request, 'borrow/check_out_borrow_list.html', context)



@login_required
def borrow_bill_pdf(request, pk):
	borrow = CheckOutBorrow.objects.get(id=pk)
	context = {
		'borrow': borrow
	}
	return render(request, 'borrow/borrow_bill_pdf.html', context)


@login_required
def borrow_list(request):
	borrow = CheckOutBorrow.objects.all().filter(status__contains="ຢືມປື້ມ")
	total_borrow = borrow.count()
	context = {
		'borrow': borrow
	}
	return render(request, 'borrow/borrow_list.html', context)



@login_required
def borrow_detail(request, pk):
	borrow = CheckOutBorrow.objects.get(id=pk)
	context = {
		'borrow': borrow
	}
	return render(request, 'borrow/borrow_detail.html', context)


@login_required
def borrow_pdf(request):
	borrow = CheckOutBorrow.objects.all()
	total_borrow = borrow.count()
	context = {
		'borrow': borrow,
		'total_borrow': total_borrow
	}
	return render(request, 'borrow/borrow_pdf.html', context)


@login_required
def borrow_bill(request, pk):
	order = CheckOutBorrow.objects.get(id=pk)

	context = {
		'order': order
	}
	return render(request, 'borrow/borrow_bill.html', context)



@login_required
def borrow_update(request, pk):
	order = CheckOutBorrow.objects.get(id=pk)
	form = BorrowUpdateForm(instance=order)

	if request.method == 'POST':
		form = BorrowUpdateForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('borrow-list')

	else:

		form = BorrowUpdateForm(instance=order)
	return render(request, 'borrow/check_out_borrow_create.html', {'form': form})



@login_required
def borrow_delete(request, pk):
	order = CheckOutBorrow.objects.get(id=pk)
	if request.method == 'POST':
		order.delete()
		return redirect('borrow-list')
	context = {'orders': order}
	return render(request, 'borrow/borrow_delete.html', context)



@login_required
def check_out_borrow_detail(request, pk):
	borrow = CheckOutBorrow.objects.get(id=pk)

	context = {
		'borrow': borrow
	}
	return render(request, 'borrow/check_out_borrow_detail.html', context)



@login_required
def reclaim_book_create(request):
	if request.method == 'POST':
		form = ReclaimBookForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('reclaim-book-list')

	else:

		form = ReclaimBookForm()
	return render(request, 'borrow/reclaim_book_create.html', {'form': form})


@login_required
def reclaim_book_update(request, pk):
	order = ReclaimBook.objects.get(id=pk)
	form = ReclaimBookForm(instance=order)

	if request.method == 'POST':
		form = ReclaimBookForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('reclaim-book-list')

	else:

		form = ReclaimBookForm(instance=order)
	return render(request, 'borrow/reclaim_book_create.html', {'form': form})


@login_required
def reclaim_book_list(request):
	reclaim = ReclaimBook.objects.all()
	total_reclaim = reclaim.count()
	context = {
		'reclaim': reclaim,
		'total_reclaim': total_reclaim
	}
	return render(request, 'borrow/reclaim_book_list.html', context)



@login_required
def reclaim_book_delete(request, pk):
	order = ReclaimBook.objects.get(id=pk)
	if request.method == 'POST':
		order.delete()
		return redirect('reclaim-book-list')
	context = {'orders': order}
	return render(request, 'borrow/reclaim_book_confirm_delete.html', context)


@login_required
def reclaim_book_pdf(request):
	reclaim = ReclaimBook.objects.all()
	total_reclaim = reclaim.count()
	context = {
		'reclaim': reclaim,
		'total_reclaim': total_reclaim
	}
	return render(request, 'borrow/reclaim_book_pdf.html', context)



@login_required
def reclaim_bill_pdf(request, pk):
	reclaim = ReclaimBook.objects.get(id=pk)

	context = {
		'reclaim': reclaim
	}
	return render(request, 'borrow/reclaim_bill_pdf.html', context)





@login_required
def book_return_create(request):
	if request.method == 'POST':
		form = BookReturnForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.employee = request.user
			instance.save()
			return redirect('book-return-list')

	else:

		form = BookReturnForm()
	return render(request, 'borrow/book_return_create.html', {'form': form})


@login_required
def return_update(request, pk):
	order = BookReturn.objects.get(id=pk)
	form = BookReturnForm(instance=order)

	if request.method == 'POST':
		form = BookReturnForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('book-return-list')
	else:

		form = BookReturnForm(instance=order)
	return render(request, 'borrow/book_return_create.html', {'form': form})



@login_required
def book_return_delete(request, pk):
	order = BookReturn.objects.get(id=pk)
	if request.method == 'POST':
		order.delete()
		return redirect('book-return-list')
	context = {'orders': order}
	return render(request, 'borrow/book_return_confirm_delete.html', context)



@login_required
def book_return_list(request):
	book = BookReturn.objects.all()
	# total_reclaim = reclaim.count()
	context = {
		'book': book,
		# 'total_reclaim': total_reclaim
	}
	return render(request, 'borrow/book_return_list.html', context)



@login_required
def book_return_pdf(request):
	borrow = BookReturn.objects.all()
	total_borrow = borrow.count()
	context = {
		'borrow': borrow,
		'total_borrow': total_borrow
	}
	return render(request, 'borrow/book_return_pdf.html', context)




@login_required
def book_return_bill_pdf(request, pk):
	book_return = BookReturn.objects.get(id=pk)

	context = {
		'book_return': book_return
	}
	return render(request, 'borrow/book_return_bill_pdf.html', context)



@login_required
def book_return_borrow(request):
	borrow = CheckOutBorrow.objects.all()
	# total_borrow = borrow.count()
	context = {
		'borrow': borrow
	}
	return render(request, 'borrow/book_return_borrow.html', context)





@login_required
def book_return_update(request, pk):
	order = CheckOutBorrow.objects.get(id=pk)
	form = ReuturnBorrowUpdateForm(instance=order)

	if request.method == 'POST':
		form = ReuturnBorrowUpdateForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('book-return-borrow')

	else:

		form = ReuturnBorrowUpdateForm(instance=order)
	return render(request, 'borrow/book_return_update.html', {'form': form})



@login_required
def date_return_out(request):
	today = date.today()
	borrow = CheckOutBorrow.objects.filter(date_return__lt=today).filter(status__contains="ຢືມປື້ມ")

	context = {
		'borrow': borrow
	}

	return render(request, 'borrow/date_return_out.html', context)



@login_required
def book_over_borrow(request):
	today = date.today()
	borrow = CheckOutBorrow.objects.filter(date_return__lt=today).filter(status__contains="ຢືມປື້ມ")

	context = {
		'borrow': borrow
	}

	return render(request, 'borrow/book_over_borrow.html', context)




@login_required
def book_over_borrow_pdf(request):
	today = date.today()
	borrow = CheckOutBorrow.objects.filter(date_return__lt=today).filter(status__contains="ຢືມປື້ມ")
	total_borrow = borrow.count()

	context = {
		'borrow': borrow,
		'total_borrow': total_borrow
	}

	return render(request, 'borrow/book_over_borrow_pdf.html', context)






@login_required
def book_over_borrow_bill(request, pk):
	order = CheckOutBorrow.objects.get(id=pk)

	context = {
		'order': order
	}
	return render(request, 'borrow/book_over_borrow_bill.html', context)
















