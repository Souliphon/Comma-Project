# Generated by Django 3.0.5 on 2020-05-26 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_point'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='members',
            options={'ordering': ['-firstname']},
        ),
        migrations.AlterModelOptions(
            name='point',
            options={'ordering': ['-id']},
        ),
    ]
