from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from .models import Profile
from django.http import HttpResponse
import csv



@login_required
def export_employee(request):
    response = HttpResponse(content_type='text/csv')
    response.write(u'\ufeff'.encode('utf-8'))
    writer = csv.writer(response)
    writer.writerow(['ລະຫັດພະນັກງານ', 'ຊື່ແທ້', 'ນາມສະກຸນ', 'ເພດ', 'ວັນເດືອນປີເກີດ', 'ເບີໂທ', 'ບ້ານ', 'ເມືອງ', 'ແຂວງ', 'ຮູບພະນັກງານ'])


    for employees in Profile.objects.all().values_list('id', 'firstname', 'surname', 'sex', 'birthday', 'tel', 'village', 'district', 'province', 'image'):
        writer.writerow(employees)

    response['Content-Disposition'] = 'attachment; filename="employees.csv"'

    return response 


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
            instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been update!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)



@login_required
def user_list(request):
    user = Profile.objects.all()
   
    context = {
        'user': user
    }
    return render(request, 'users/user_list.html', context)


@login_required
def employee_pdf(request):
    user = Profile.objects.all()
    total_employee = user.count()
   
    context = {
        'user': user,
        'total_employee': total_employee
    }
    return render(request, 'users/employee_pdf.html', context)




