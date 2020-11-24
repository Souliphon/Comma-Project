from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookOrderForm
from .models import BookOrder
from booktype.models import BookStore
from django.contrib.auth.models import User
# from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import csv
from django.template.loader import get_template
from django.views import View
import xhtml2pdf.pisa as pisa 
from io import BytesIO
from django.utils import timezone



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


# #Opens up page as PDF
# class BookOrderPDFView(LoginRequiredMixin, View):
# 	def get(self, request, *args, **kwargs):
# 		bookorders = BookOrder.objects.all()
# 		today = timezone.now()
# 		# print (booktype.id)
# 		params = {
# 			'today': today,
# 			'bookorders': bookorders,
# 			'request': request
# 		}

# 		return Render.render('bookorder/bookorder_pdf_template.html', params)


# Create your views here.
@login_required
def export_bookorder(request):
	response = HttpResponse(content_type='text/csv')
	response.write(u'\ufeff'.encode('utf-8'))
	writer = csv.writer(response)
	writer.writerow(['ລະຫັດການສັ່ງຊື້ປື້ມ', 'ວັນເດືອນປີສັ່ງຊື້ປື້ມ', 'ຈຳນວນ', 'ລະຫັດຮ້ານຂາຍປື້ມ', 'ລະຫັດພະນັກງານ'])

	for bookorder in BookOrder.objects.all().values_list('id', 'date_order', 'amount', 'bookstore', 'employee'):
		writer.writerow(bookorder)

	response['Content-Disposition'] = 'attachment; filename="bookorders.csv"'

	return response 



@login_required
def order_list(request):
	bookorder = BookOrder.objects.all()
	# total_bookorder = bookorder.count()

	# query = request.GET.get('q', None)
	# if query is not None:
	# 	bookorder = bookorder.filter(
	# 		Q(id__icontains=query)
	# 	)

	# paginator = Paginator(bookorder, 5)
	# page = request.GET.get('page', 1)
	# bookorder = paginator.get_page(page)

	# try:
	# 	bookorders = paginator.page(page)
	# except PageNotAnInteger:
	# 	bookorders = paginator.page(1)
	# except EmptyPage:
	# 	bookorders = paginator.page(paginator.num_pages)


	context = {
		'bookorders': bookorder,
		# 'total_bookorder': total_bookorder
	}
	return render(request, 'bookorder/order_list.html', context)


@login_required
def order_pdf(request):
	bookorder = BookOrder.objects.all()
	total_bookorder = bookorder.count()


	context = {
		'bookorders': bookorder,
		'total_bookorder': total_bookorder
	}
	return render(request, 'bookorder/order_pdf.html', context)





@login_required
def order_create(request):
	if request.method == 'POST':
		form = BookOrderForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.employee = request.user
			instance.save()
			return redirect('order-list')

	else:

		form = BookOrderForm()
	return render(request, 'bookorder/order_create.html', {'form': form})


@login_required
def order_update(request, pk):
	order = BookOrder.objects.get(id=pk)
	form = BookOrderForm(instance=order)

	if request.method == 'POST':
		form = BookOrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('order-list')

	else:

		form = BookOrderForm(instance=order)
	return render(request, 'bookorder/order_create.html', {'form': form})



@login_required
def order_delete(request, pk):
	order = BookOrder.objects.get(id=pk)
	if request.method == 'POST':
		order.delete()
		return redirect('order-list')
	context = {'orders': order}
	return render(request, 'bookorder/order_delete.html', context)



@login_required
def bookorder_bill_pdf(request, pk):
	order = BookOrder.objects.get(id=pk)

	context = {
		'order': order
	}
	return render(request, 'bookorder/order_bill_pdf.html', context)


# @login_required
# def export_bill_bookorder(request, pk):
# 	response = HttpResponse(content_type='text/csv')
# 	response.write(u'\ufeff'.encode('utf-8'))
# 	writer = csv.writer(response)
# 	writer.writerow(['ລະຫັດການສັ່ງຊື້ປື້ມ', 'ວັນເດືອນປີສັ່ງຊື້ປື້ມ', 'ຈຳນວນ', 'ລະຫັດຮ້ານຂາຍປື້ມ', 'ລະຫັດພະນັກງານ'])

# 	bookorder = BookOrder.objects.get(id=pk).values_list('id', 'date_order', 'amount', 'bookstore', 'employee')
# 	writer.writerow(bookorder)

# 	response['Content-Disposition'] = 'attachment; filename="bill_bookorder.csv"'

# 	return response 














