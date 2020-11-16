from django.db import models
from phone_field import PhoneField
from PIL import Image
from django.urls import reverse
# Create your models here.
sex_choices = (
		("MALE", "Male"),
		("FEMALE", "Female"),
	)

vt_districts = (
		("CHANTHABULY", "Chanthabuly"),
		("SIKHOTTABONG", "Sikhottabong"),
		("XAYSETHA", "Xaysetha"),
		("SISATTANAK", "Sisattanak"),
		("XAYTHANY", "Xaythany"),
	)



class Members(models.Model):
	firstname = models.CharField(max_length=20)
	surname = models.CharField(max_length=20)
	sex = models.CharField(max_length=6, choices=sex_choices, default="MALE")
	birthday = models.DateField(max_length=8, help_text='YY-MM-DD')
	tel = PhoneField(blank=True, help_text='Contact phone number e.g 2055667788-856', unique=True)
	email = models.EmailField(max_length=30)
	village = models.CharField(max_length=20)
	district = models.CharField(max_length=12, choices=vt_districts, default="SISATTANAK")
	province = models.CharField(max_length=17, default="Vientiane Capital")
	image = models.ImageField(null=True, upload_to='member_profile_pics', help_text='Fill in your member profile')
	image1 = models.ImageField(null=True, upload_to='member_identity_pics', help_text='Fill in your identity card')

	def __str__(self):
		return self.firstname

	def save(self, *args, **kwargs):
		super(Members, self).save(*args, **kwargs)

		img = Image.open(self.image.path)
		img1 = Image.open(self.image1.path)

		if img.height > 300 or img.width > 300 or img1.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

			output_size1 = (300, 300)
			img1.thumbnail(output_size1)
			img1.save(self.image1.path)

	def get_absolute_url(self):
		return reverse('members-detail', kwargs={'pk': self.pk})

	class Meta:
		ordering = ['-id']


class Point(models.Model):
	amount = models.IntegerField(null=True, blank=True)
	member = models.OneToOneField(Members, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.id}'

	def get_absolute_url(self):
		return reverse('point-detail', kwargs={'pk': self.pk})

	class Meta:
		ordering = ['-id']

		

		
