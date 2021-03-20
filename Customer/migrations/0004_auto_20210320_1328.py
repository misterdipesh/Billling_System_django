# Generated by Django 3.1.7 on 2021-03-20 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0003_auto_20210320_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_email',
            field=models.EmailField(default='xyz@abc.com', max_length=254, null=True, unique=True),
        ),
    ]
