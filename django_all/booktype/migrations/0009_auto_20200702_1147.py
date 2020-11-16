# Generated by Django 3.0.5 on 2020-07-02 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktype', '0008_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('ວ່າງ', 'ວ່າງ'), ('ຖືກຢືມ', 'ຖຶກຢືມ')], default='ວ່າງ', max_length=12),
        ),
    ]