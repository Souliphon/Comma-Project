# Generated by Django 3.0.5 on 2020-06-16 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0005_auto_20200611_2159'),
        ('borrow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckOutBorrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_rent', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_return', models.DateField(help_text='YY-MM-DD', max_length=8)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='borrow.BorrowBook')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Members')),
            ],
        ),
    ]
