# Generated by Django 4.0.6 on 2022-07-26 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='meta_description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_description',
            field=models.TextField(max_length=500),
        ),
    ]
