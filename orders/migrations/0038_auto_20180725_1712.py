# Generated by Django 2.0.6 on 2018-07-25 14:12

from django.db import migrations, models
import orders.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0037_auto_20180725_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='phone_number',
            field=models.PositiveIntegerField(null=True, validators=[orders.models.validate_number]),
        ),
    ]