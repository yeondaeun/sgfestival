# Generated by Django 2.0.13 on 2019-04-27 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtruck', '0003_foodtruck_truckinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='writer',
        ),
    ]
