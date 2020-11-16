from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Members, Point
from .forms import MembersForm, PointForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse
import csv
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
@login_required
def export_member(request):
	response = HttpResponse(content_type='text/csv')
	response.write(u'\ufeff'.encode('utf-8'))
	writer = csv.writer(response)
	writer.writerow(['ລະຫັດສະມາຊິກ', 'ຊື່ແທ້', 'ນາມສະກຸນ', 'ເພດ', 'ວັນເດືອນປີເກີດ', 'ເບີໂທ', 'ອີເມວ', 'ບ້ານ', 'ເມືອງ', 'ແຂວງ', 'ຮູບສະມາຊິກ', 'ຮູບບັດປະຈຳຕົວ'])

	for member in Members.objects.all().values_list('id', 'firstname', 'surname', 'sex', 'birthday', 'tel', 'email', 'village', 'district', 'province', 'image', 'image1'):
		writer.writerow(member)

	response['Content-Disposition'] = 'attachment; filename="members.csv"'

	return response 


@login_required
def export_point(request):
	response = HttpResponse(content_type='text/csv')
	response.write(u'\ufeff'.encode('utf-8'))
	writer = csv.writer(response)
	writer.writerow(['ລະຫັດສະຖິຕິການຊື້ຈຳນວນສິນຄ້າ', 'ຈຳນວນການຊື້ສິນຄ້າ', 'ລະຫັດສະມາຊິກ'])

	for points in Point.objects.all().values_list('id', 'amount', 'member'):
		writer.writerow(points)

	response['Content-Disposition'] = 'attachment; filename="points.csv"'

	return response 


@login_required
def export_member_allow(request):
	response = HttpResponse(content_type='text/csv')
	response.write(u'\ufeff'.encode('utf-8'))
	writer = csv.writer(response)
	writer.writerow(['ລະຫັດສະຖິຕິການຊື້ຈຳນວນສິນຄ້າ', 'ຈຳນວນການຊື້ສິນຄ້າ', 'ລະຫັດສະມາຊິກ'])

	for points in Point.objects.filter(amount__gte=5).values_list('id', 'amount', 'member'):
		writer.writerow(points)

	response['Content-Disposition'] = 'attachment; filename="export_member_allow.csv"'

	return response 




@login_required
def member_allow(request):
	point = Point.objects.filter(amount__gte=5)

	context = {
		'points': point 
	}

	return render(request, 'members/member_allow.html', context)

@login_required
def member_allow_pdf(request):
	point = Point.objects.filter(amount__gte=5)
	total_allow = point.count()

	context = {
		'points': point,
		'total_allow': total_allow
	}

	return render(request, 'members/member_allow_pdf.html', context)


@login_required
def select_point(request):
	point = Point.objects.filter(amount__gte=5)

	context = {
		'points': point 
	}

	return render(request, 'members/select_point.html', context)


@login_required
def cut_point(request, pk):
	order = Point.objects.get(id=pk)
	if request.method == 'POST':
		if order.amount < 5:
			return redirect('/')
		else:
			b = 4
			c = order.amount - b
			order.amount = c 
			order.save()
			return redirect('select-book-borrow')

	
	context = {'orders': order}
	return render(request, 'members/confirm_cut_point.html', context)


# @login_required
# def cut_point(request, pk):
# 	point = Point.objects.get(id=pk)

# 	if point.amount <= 3:
# 		return redirect('/')
# 	else:
# 		b = 3
# 		c = point.amount - b
# 		point.amount = c 
# 		point.save()

# 	context = {
# 		'point': point
# 	}

# 	return render(request, 'members/cut_point.html', context)



@login_required
def point_list(request):
	# request.session.set_expiry(1200)

	point = Point.objects.all()
	# total_point = point.count()

	# query = request.GET.get('q', None)
	# if query is not None:
	# 	point = point.filter(
	# 		Q(id__icontains=query)
	# 	)

	# paginator = Paginator(point, 5)
	# page = request.GET.get('page', 1)
	# point = paginator.get_page(page)

	# try:
	# 	points = paginator.page(page)
	# except PageNotAnInteger:
	# 	points = paginator.page(1)
	# except EmptyPage:
	# 	points = paginator.page(paginator.num_pages)

	# request.session['amount_point'] = Point.objects.filter(amount__gte=2)

	context = {
		'points': point,
		# 'total_point': total_point
	}
	return render(request, 'members/point_list.html', context)



@login_required
def point_pdf(request):

	point = Point.objects.all()
	total_point = point.count()

	context = {
		'points': point,
		'total_point': total_point
	}
	return render(request, 'members/point_pdf.html', context)




@login_required
def point_create(request):
	if request.method == 'POST':
		form = PointForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('point-list')

	else:
		form = PointForm()
	return render(request, 'members/point_create.html', {'form': form})

@login_required
def point_update(request, pk):
	order = Point.objects.get(id=pk)
	form = PointForm(instance=order)

	if request.method == 'POST':
		form = PointForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('point-list')

	else:

		form = PointForm(instance=order)
	return render(request, 'members/point_create.html', {'form': form})

@login_required
def point_delete(request, pk):
	order = Point.objects.get(id=pk)
	if request.method == 'POST':
		order.delete()
		return redirect('point-list')
	context = {'orders': order}
	return render(request, 'members/point_confirm_delete.html', context)


# # member for customers
# def member_register(request):
# 	if request.method == 'POST':
# 		form = MembersForm(request.POST or None, request.FILES or None)
# 		if form.is_valid():
# 			form.save()
# 			firstname = form.cleaned_data.get('firstname')
# 			return redirect('thanks')
# 	else:
# 		form = MembersForm(request.POST or None, request.FILES or None)

# 	return render(request,'members/member_register.html', {'form': form})


def thanks(request):
	return render(request, 'members/thanks.html', {'title': 'Thanks'})

# member for users
@login_required
def member_view_more(request):
	member = Members.objects.all()#.order_by('-firstname')
	# total_member = member.count()

	context = {
		'members': member,
		# 'total_member': total_member,
		
	}
	return render(request, 'members/member_view_more.html', context)



@login_required
def member_list(request):
	member = Members.objects.all()#.order_by('-firstname')
	# total_member = member.count()

	# query = request.GET.get('q', None)
	# if query is not None:
	# 	member = member.filter(
	# 		Q(id__icontains=query)
	# 	)

	# paginator = Paginator(member, 4)
	# page = request.GET.get('page', 1)
	# member = paginator.get_page(page)

	# try:
	# 	members = paginator.page(page)
	# except PageNotAnInteger:
	# 	members = paginator.page(1)
	# except EmptyPage:
	# 	members = paginator.page(paginator.num_pages)

	

	context = {
		'members': member,
		# 'total_member': total_member,
		
	}
	return render(request, 'members/members_list.html', context)




@login_required
def member_pdf(request):
	member = Members.objects.all()#.order_by('-firstname')
	total_member = member.count()

	context = {
		'members': member,
		'total_member': total_member,
		
	}
	return render(request, 'members/members_pdf.html', context)



@login_required
def members_register(request):
	if request.method == 'POST':
		form = MembersForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			form.save()
			return redirect('members-list')
	else:
		form = MembersForm(request.POST or None, request.FILES or None)

	return render(request, 'members/member_register.html', {'form': form})



@login_required
def member_update(request, pk):
	order = Members.objects.get(id=pk)
	form = MembersForm(request.POST or None, request.FILES or None, instance=order)

	if request.method == 'POST':
		form = MembersForm(request.POST or None, request.FILES or None, instance=order)
		if form.is_valid():
			form.save()
			return redirect('members-list')

	else:

		form = MembersForm(request.POST or None, request.FILES or None, instance=order)
	return render(request, 'members/member_register.html', {'form': form})




@login_required
def member_delete(request, pk):
	order = Members.objects.get(id=pk)
	if request.method == 'POST':
		order.delete()
		return redirect('members-list')
	context = {'orders': order}
	return render(request, 'members/members_confirm_delete.html', context)





@login_required
def member_detail(request, pk):
	member = Members.objects.get(id=pk)

	context = {
		'member': member
	}
	return render(request, 'members/members_detail.html', context)




@login_required
def member_pdf_card(request, pk):
	point = Point.objects.get(id=pk)

	context = {
		'point': point
	}
	return render(request, 'members/member_pdf_card.html', context)










