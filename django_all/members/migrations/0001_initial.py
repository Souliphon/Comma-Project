# Generated by Django 3.0.5 on 2020-04-25 09:32

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('sex', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='MALE', max_length=6)),
                ('birthday', models.DateField(help_text='YY-MM-DD', max_length=8)),
                ('tel', phone_field.models.PhoneField(blank=True, help_text='Contact phone number e.g 0255667788-856', max_length=31, unique=True)),
                ('email', models.EmailField(max_length=30)),
                ('village', models.CharField(max_length=20)),
                ('district', models.CharField(choices=[('CHANTHABULY', 'Chanthabuly'), ('SIKHOTTABONG', 'Sikhottabong'), ('XAYSETHA', 'Xaysetha'), ('SISATTANAK', 'Sisattanak'), ('XAYTHANY', 'Xaythany')], default='SISATTANAK', max_length=12)),
                ('province', models.CharField(default='Vientiane Capital', max_length=17)),
                ('image', models.ImageField(blank=True, null=True, upload_to='member_profile_pics')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='member_identity_pics')),
            ],
        ),
    ]
