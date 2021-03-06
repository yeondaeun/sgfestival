# Generated by Django 2.0.13 on 2019-04-27 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('c1', models.IntegerField()),
                ('c2', models.IntegerField()),
                ('c3', models.IntegerField()),
                ('c4', models.IntegerField()),
                ('c5', models.IntegerField()),
                ('c6', models.IntegerField()),
                ('c7', models.IntegerField()),
                ('c8', models.IntegerField()),
                ('c9', models.IntegerField()),
                ('c10', models.IntegerField()),
                ('c11', models.IntegerField()),
                ('c12', models.IntegerField()),
                ('c13', models.IntegerField()),
                ('c14', models.IntegerField()),
                ('c15', models.IntegerField()),
                ('c16', models.IntegerField()),
                ('c17', models.IntegerField()),
                ('c18', models.IntegerField()),
                ('c19', models.IntegerField()),
                ('c20', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('c1', models.CharField(max_length=300)),
                ('c2', models.CharField(max_length=300)),
                ('c3', models.CharField(max_length=300)),
                ('c4', models.CharField(max_length=300)),
                ('answer', models.IntegerField()),
            ],
        ),
    ]
