# Generated by Django 2.1.5 on 2019-05-14 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtruck', '0004_auto_20190427_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtruck',
            name='truckphoto',
            field=models.CharField(blank=True, default='', max_length=2000, null=True),
        ),
    ]
