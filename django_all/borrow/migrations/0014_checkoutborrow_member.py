# Generated by Django 3.0.5 on 2020-06-25 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20200611_2159'),
        ('borrow', '0013_auto_20200625_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutborrow',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.Members'),
        ),
    ]