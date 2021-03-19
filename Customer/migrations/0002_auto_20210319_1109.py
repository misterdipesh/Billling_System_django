# Generated by Django 3.1.7 on 2021-03-19 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_number',
            field=models.CharField(max_length=20, unique=True, verbose_name='Phone Number'),
        ),
    ]
