# Generated by Django 2.1.4 on 2019-04-07 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_auto_20190406_1307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biditems',
            options={'ordering': ('?',)},
        ),
        migrations.AddField(
            model_name='biditems',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='biditems',
            name='won',
            field=models.BooleanField(default=False),
        ),
    ]
