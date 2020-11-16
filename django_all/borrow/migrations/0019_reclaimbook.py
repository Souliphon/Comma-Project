# Generated by Django 3.0.5 on 2020-07-07 15:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0018_auto_20200703_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReclaimBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reclaim', models.DateTimeField(default=django.utils.timezone.now)),
                ('borrow', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='borrow.CheckOutBorrow')),
            ],
        ),
    ]