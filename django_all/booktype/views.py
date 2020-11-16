from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from .forms import BookTypeForm, BookForm, BookStoreForm, BookUpdateBorrowForm
from .models import BookType, Book, BookStore
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
import csv
from django.template.loader import get_template
from django.views import View
import xhtml2pdf.pisa as pisa 
from io import BytesIO
from django.utils import timezone

# import io
# from django.http import FileResponse
# from reportlab.pdfgen import canvas
# from reportlab.pdfbase.ttfonts import TTFont 
# from reportlab.pdfbase import pdfmetrics 
# from reportlab.lib import colors




# title = 'ສາທາລະນະລັດ ປະຊາທິປະໄຕ ປະຊາຊົນລາວ'
# title1 = 'ສັນຕິພາບ ເອກະລາດ ປະຊາທິປະໄຕ ເອກະພາບ ວັດທະນະຖາວອນ'

# subtitle = 'ໝັງສືລາຍງານຂໍ້ມູນ'



# def some_view(request):

# 	buffer = io.BytesIO()

# 	p = canvas.Canvas(buffer)

# 	pdfmetrics.registerFont(
# 			TTFont('Saysettha OT', 'saysettha_ot.ttf')
# 		)

# 	p.setFont('Saysettha OT', 12)

# 	p.setTitle('Hello')

# 	p.drawCentredString(300, 790, title)

# 	p.drawCentredString(300, 770, title1)

# 	p.setFillColorRGB(0, 0, 255)

# 	p.drawCentredString(300, 720, subtitle)

# 	booktypes = BookType.objects.all()

# 	for i in booktypes:
# 		a = i.id
# 		b = i.name 
# 		c = i.zone_number


# 		p.drawString(100, 600, str(a))

# 		p.drawString(200, 600, b)

# 		p.drawString(400, 600, c)


# 	p.showPage()

# 	p.save()

# 	buffer.seek(0)

	
# 	return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


# class Render:
# 	@staticmethod
# 	def render(path: str, params: dict):
# 		template = get_template(path)
# 		html = template.render(params)
# 		response = BytesIO()
# 		pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), response, encoding='UTF-8')
# 		if not pdf.err:
# 			return HttpResponse(response.getvalue(), content_type='application/pdf')
# 		else:
# 			return HttpResponse("Error Rendering PDF", status=400)

# #Opens up page as PDF
# class BookTypePDFView(LoginRequiredMixin, View):
# 	def get(self, request, *args, **kwargs):
# 		booktypes = BookType.objects.all()
# 		today = timezone.now()
# 		params = {
# 			'today': today,
# 			'booktypes': booktypes,
# 			'request': request
# 		}

# 		return Render.render('booktype/booktype_pdf_template.html', params)

# class BookPDFView(LoginRequiredMixin, View):
# 	def get(self, request, *args, **kwargs):
# 		books = Book.objects.all()
# 		today = timezone.now()
# 		params = {
# 			'today': today,
# 			'books': books,
# 			'request': request
# 		}

# 		return Render.render('booktype/pdf.html', params)

# class BookStorePDFView(LoginRequiredMixin, View):
# 	def get(self, request, *args, **kwargs):
# 		bookstores = BookStore.objects.all()
# 		today = timezone.now()
# 		params = {
# 			'today': today,
# 			'bookstores': bookstores,
# 			'request': request
# 		}

# 		return Render.render('booktype/bookstore_pdf_template.html', params)




@login_required
def export_booktype(request):
	response = HttpResponse(content_type='text/csv')
	response.write(u'\ufeff'.encode('utf-8'))
	writer = csv.writer(response)
	# writer.writerow(['ສາທາລະນະລັດ ປະຊາທິປະໄຕ ປະຊາຊົນລາວ'])
	writer.writerow(['ລະຫັດປະເພດປື້ມ', 'ຊື່ປະເພດປື້ມ', 'ເລກໝວດເອກະສານ'])

	for booktypes in BookType.objects.all().values_list('id', 'name', 'zone_number'):
		writer.writerow(booktypes)

	response['Content-Disposition'] = 'attachment; filename="booktypes.csv"'

	return response 


@login_required
def export_book(request):
	response = HttpResponse(content_type='text/csv')
	response.write(u'\ufeff'.encode('utf-8'))
	writer = csv.writer(response)
	writer.writerow(['ລະຫັດປື້ມ', 'ຊື່ເລື່ອງ', 'ຫົວເລື່ອງ', 'ຜູ້ແຕ່ງຫຼັກ', 'ຜູ້ຕ່າງທ່ານອື່ນ', 'ພາສາຕົ້ນສະບັບ', 'ລາຄາ', 'ຈຳນວນໜ້າ', 'ລະຫັດກຳກັບປື້ມ', 'ສະຖານະປື້ມ', 'ວັນເດືອນປີເກັບຂໍ້ມູນປື້ມ', 'ລະຫັດປະເພດປື້ມ'])

	for book in Book.objects.all().values_list('id', 'title', 'subject_heading', 'primary_author', 'coauthor', 'original_language', 'price', 'page_element', 'ISBN', 'status', 'date_created', 'booktype'):
		writer.writerow(book)

	response['Content-Disposition'] = 'attachment; filename="books.csv"'

	return response 


@login_required
def export_bookstore(request):
	response = HttpResponse(content_type='text/csv')
	response.write(u'\ufeff'.encode('utf-8'))
	writer = csv.writer(response)
	writer.writerow(['ລະຫັດຮ້ານຂາຍປື້ມ', 'ຊື່ຮ້ານຂາຍປື້ມ', 'ເບີໂທ', 'ອີເມວ', 'ບ້ານ', 'ເມືອງ', 'ແຂວງ'])

	for bookstores in BookStore.objects.all().values_list('id', 'name', 'tel', 'email', 'village', 'district', 'province'):
		writer.writerow(bookstores)

	response['Content-Disposition'] = 'attachment; filename="bookstores.csv"'

	return response 




# book type
@login_required
def booktype_list(request):
	booktype = BookType.objects.all()
	# total_booktype = booktype.count()

	# query = request.GET.get('q', None)
	# if query is not None:
	# 	booktype = booktype.filter(
	# 		Q(id__icontains=query)
	# 	)

	# paginator = Paginator(booktype, 5)
	# page = request.GET.get('page', 1)
	# booktype = paginator.get_page(page)

	# try:
	# 	booktypes = paginator.page(page)
	# except PageNotAnInteger:
	# 	booktypes = paginator.page(1)
	# except EmptyPage:
	# 	booktypes = paginator.page(paginator.num_pages)


	context = {
		'booktypes': booktype,
		# 'total_booktype': total_booktype
	}
	return render(request, 'booktype/booktype_list.html', context)



@login_required
def booktype_pdf(request):
	booktype = BookType.objects.all()
	total_booktype = booktype.count()

	context = {
		'booktypes': booktype,
		'total_booktype': total_booktype
	}
	return render(request, 'booktype/booktype_pdf.html', context)



@login_required
def booktype_create(request):
	if request.method == 'POST':
		form = BookTypeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('booktype-list')

	else:

		form = BookTypeForm()
	return render(request, 'booktype/booktype_create.html', {'form': form})

@login_required
def booktype_update(request, pk):
	order = BookType.objects.get(id=pk)
	form = BookTypeForm(instance=order)

	if request.method == 'POST':
		form = BookTypeForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('booktype-list')

	else:
		form = BookTypeForm(instance=order)

	return render(request, 'booktype/booktype_create.html', {'form': form})


@login_required
def booktype_delete(request, pk):
	order = BookType.objects.get(id=pk)
	if request.method == 'POST':
		order.delete()
		return redirect('booktype-list')
	context = {'orders': order}
	return render(request, 'booktype/booktype_confirm_delete.html', context)

# bookstore
@login_required
def bookstore_list(request):
	bookstore = BookStore.objects.all()
	# total_bookstore = bookstore.count()

	# query = request.GET.get('q', None)
	# if query is not None:
	# 	bookstore = bookstore.filter(
	# 		Q(id__icontains=query)
	# 	)

	# paginator = Paginator(bookstore, 5)
	# page = request.GET.get('page', 1)
	# bookstore = paginator.get_page(page)

	# try:
	# 	bookstores = paginator.page(page)
	# except PageNotAnInteger:
	# 	bookstores = paginator.page(1)
	# except EmptyPage:
	# 	bookstores = paginator.page(paginator.num_pages)


	context = {
		'bookstores': bookstore,
		# 'total_bookstore': total_bookstore
	}
	return render(request, 'booktype/bookstore_list.html', context)

@login_required
def bookstore_pdf(request):
	bookstore = BookStore.objects.all()
	total_bookstore = bookstore.count()

	context = {
		'bookstores': bookstore,
		'total_bookstore': total_bookstore
	}
	return render(request, 'booktype/bookstore_pdf.html', context)




@login_required
def bookstore_create(request):
	if request.method == 'POST':
		form = BookStoreForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('bookstore-list')

	else:

		form = BookStoreForm()
	return render(request, 'booktype/bookstore_create.html', {'form': form})

@login_required
def bookstore_update(request, pk):
	order = BookStore.objects.get(id=pk)
	form = BookStoreForm(instance=order)

	if request.method == 'POST':
		form = BookStoreForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('bookstore-list')

	else:

		form = BookStoreForm(instance=order)
	return render(request, 'booktype/bookstore_create.html', {'form': form})

@login_required
def bookstore_delete(request, pk):
	order = BookStore.objects.get(id=pk)
	if request.method == 'POST':
		order.delete()
		return redirect('bookstore-list')
	context = {'orders': order}
	return render(request, 'booktype/bookstore_confirm_delete.html', context)

# book
@login_required
def book_list(request):
	book = Book.objects.all()
	# total_book = book.count()

	# query = request.GET.get('q', None)
	# if query is not None:
	# 	book = book.filter(
	# 		Q(id__icontains=query) |
	# 		Q(title__icontains=query)
	# 	)

	# paginator = Paginator(book, 5)
	# page = request.GET.get('page', 1)
	# book = paginator.get_page(page)

	# try:
	# 	books = paginator.page(page)
	# except PageNotAnInteger:
	# 	books = paginator.page(1)
	# except EmptyPage:
	# 	books = paginator.page(paginator.num_pages)


	context = {
		'books': book,
		# 'total_book': total_book
	}
	return render(request, 'booktype/book_list.html', context)





# book
@login_required
def book_detail(request, pk):
	book = Book.objects.get(id=pk)

	context = {
		'book': book
	}
	return render(request, 'booktype/book_detail.html', context)


@login_required
def book_pdf(request):
	book = Book.objects.all()
	total_book = book.count()

	context = {
		'books': book,
		'total_book': total_book
	}
	return render(request, 'booktype/book_pdf.html', context)



@login_required
def book_create(request):
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('book-list')

	else:

		form = BookForm(request.POST)
	return render(request, 'booktype/book_create.html', {'form': form})

@login_required
def book_update(request, pk):
	order = Book.objects.get(id=pk)
	form = BookForm(instance=order)

	if request.method == 'POST':
		form = BookForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('book-list')

	else:

		form = BookForm(instance=order)
	return render(request, 'booktype/book_create.html', {'form': form})

# book update borrow
@login_required
def book_update_borrow(request, pk):
	order = Book.objects.get(id=pk)
	form = BookUpdateBorrowForm(instance=order)

	if request.method == 'POST':
		form = BookUpdateBorrowForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('select-book-borrow')

	else:

		form = BookUpdateBorrowForm(instance=order)
	return render(request, 'booktype/book_borrow_update.html', {'form': form})


# @login_required
# def book_detail(request, pk):
# 	book = book.objects.get(id=pk)

# 	context = {
# 		'book': book
# 	}
# 	return render(request, 'booktype/book_detail.html', context)



@login_required
def book_delete(request, pk):
	order = Book.objects.get(id=pk)
	if request.method == 'POST':
		order.delete()
		return redirect('book-list')
	context = {'orders': order}
	return render(request, 'booktype/book_confirm_delete.html', context)



#select book borrow
@login_required
def select_book_borrow(request):
	book = Book.objects.all()
	# total_book = book.count()

	# query = request.GET.get('q', None)
	# if query is not None:
	# 	book = book.filter(
	# 		Q(id__icontains=query) |
	# 		Q(title__icontains=query)
	# 	)

	# paginator = Paginator(book, 5)
	# page = request.GET.get('page', 1)
	# book = paginator.get_page(page)

	# try:
	# 	books = paginator.page(page)
	# except PageNotAnInteger:
	# 	books = paginator.page(1)
	# except EmptyPage:
	# 	books = paginator.page(paginator.num_pages)


	context = {
		'books': book,
		# 'total_book': total_book
	}
	return render(request, 'booktype/select_book_borrow.html', context)



#select book borrow
@login_required
def return_borrow_stauts(request):
	book = Book.objects.all()
	# total_book = book.count()

	# query = request.GET.get('q', None)
	# if query is not None:
	# 	book = book.filter(
	# 		Q(id__icontains=query) |
	# 		Q(title__icontains=query)
	# 	)

	# paginator = Paginator(book, 5)
	# page = request.GET.get('page', 1)
	# book = paginator.get_page(page)

	# try:
	# 	books = paginator.page(page)
	# except PageNotAnInteger:
	# 	books = paginator.page(1)
	# except EmptyPage:
	# 	books = paginator.page(paginator.num_pages)


	context = {
		'books': book,
		# 'total_book': total_book
	}
	return render(request, 'booktype/return_borrow_stauts.html', context)



# book return update borrow
@login_required
def return_status_update(request, pk):
	order = Book.objects.get(id=pk)
	form = BookUpdateBorrowForm(instance=order)

	if request.method == 'POST':
		form = BookUpdateBorrowForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('return-borrow-stauts')

	else:

		form = BookUpdateBorrowForm(instance=order)
	return render(request, 'booktype/return_status_update.html', {'form': form})
















