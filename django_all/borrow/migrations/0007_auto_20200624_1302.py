# Generated by Django 3.0.5 on 2020-06-24 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20200611_2159'),
        ('borrow', '0006_checkoutborrow_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutborrow',
            name='point',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Point'),
        ),
    ]
