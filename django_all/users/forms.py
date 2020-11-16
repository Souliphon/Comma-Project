from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username',
        'email',
        'password1', 
        'password2']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = [
		'image',
		'firstname',
		'surname',
		'sex',
		'tel',
		'village',
		'district',
		'province',
		'birthday'	
		]
		labels = {
			'image': 'ຮູບສ່ວນຕົວ',
			'firstname': 'ຊື່ແທ້',
			'surname': 'ນາມສະກຸນ',
			'sex': 'ເພດ',
			'tel': 'ເບີໂທ',
			'village': 'ບ້ານ',
			'district': 'ເມືອງ',
			'province': 'ແຂວງ',
			'birthday': 'ວັນເດືອນປີເກີດ',
		}
