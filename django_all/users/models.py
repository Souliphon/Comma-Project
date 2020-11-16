from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from phone_field import PhoneField
# Create your models here.

sex_choices = (
		("ຊາຍ", "ຊາຍ"),
		("ຍິງ", "ຍິງ"),
	)

vt_districts = (
		("ຈັນທະບູລິ", "ຈັນທະບູລິ"),
		("ສີໂຄດຕະບອງ", "ສີໂຄດຕະບອງ"),
		("ໄຊເສດຖາ", "ໄຊເສດຖາ"),
		("ສີສັດຕະນາກ", "ສີສັດຕະນາກ"),
		("ໄຊທານີ", "ໄຊທານີ"),
	)



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	firstname = models.CharField(max_length=20, null=True, blank=True)
	surname = models.CharField(max_length=20, null=True, blank=True)
	sex = models.CharField(max_length=3, choices=sex_choices, default="ຊາຍ", null=True, blank=True)
	tel = PhoneField(blank=True, help_text='Contact phone number e.g 2055667788-856', null=True)
	village = models.CharField(max_length=20, null=True, blank=True)
	district = models.CharField(max_length=12, choices=vt_districts, default="ຈັນທະບູລິ", null=True, blank=True)
	province = models.CharField(max_length=17, default="ນະຄອນຫຼວງວຽງຈັນ", null=True, blank=True)
	birthday = models.DateField(help_text='YY-MM-DD', null=True, blank=True)

	def __str__(self):
		return f'{self.user.username} Profile'


	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)