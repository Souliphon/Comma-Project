# Generated by Django 3.0.5 on 2020-08-23 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktype', '0013_auto_20200715_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='coauthor',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]