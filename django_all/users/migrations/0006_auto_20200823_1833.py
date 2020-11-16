# Generated by Django 3.0.5 on 2020-08-23 11:33

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200703_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tel',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number e.g 2055667788-856', max_length=31, null=True),
        ),
    ]
