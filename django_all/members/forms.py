from django.forms import ModelForm
from .models import Members, Point
from django import forms

class MembersForm(forms.ModelForm):
	class Meta:
		model = Members
		fields = [
			'firstname',
			'surname',
			'sex',
			'birthday',
			'tel',
			'email',
			'village',
			'district',
			'province',
			'image',
			'image1',
		]
		labels = {
			'firstname': 'ຊື່ສະມາຊິກ',
			'surname': 'ນາມສະກຸນ',
			'sex': 'ເພດ',
			'birthday': 'ວັນເດືອນປີເກີດ',
			'tel': 'ເບີໂທ',
			'email': 'ອີເມວ',
			'village': 'ບ້ານ',
			'district': 'ເມືອງ',
			'province': 'ແຂວງ',
			'image': 'ຮູບສະມາຊິກ',
			'image1': 'ຮູບບັດປະຈຳຕົວ',
		}

		widgets = {
			'firstname': forms.TextInput(attrs={'class': 'form-control'}),
			'surname': forms.TextInput(attrs={'class': 'form-control'}),
			'sex': forms.Select(attrs={'class': 'form-control'}),
			'birthday': forms.TextInput(attrs={'class': 'form-control'}),
			'tel': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.TextInput(attrs={'class': 'form-control'}),
			'village': forms.TextInput(attrs={'class': 'form-control'}),
			'district': forms.Select(attrs={'class': 'form-control'}),
			'province': forms.TextInput(attrs={'class': 'form-control'}),
			# 'image': forms.File(attrs={'class': 'form-control'}),
			# 'image1': forms.TextInput(attrs={'class': 'form-control'}),
		}

class PointForm(ModelForm):
	class Meta:
		model = Point
		fields = [
			'amount',
			'member'
		]
		labels = {
			'amount': 'ຈຳນວນການຊື້ສິນຄ້າ',
			'member': 'ສະມາຊິກ',
		}

