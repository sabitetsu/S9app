# Generated by Django 3.2.8 on 2022-01-16 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SighModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigh', models.CharField(max_length=500)),
                ('same', models.IntegerField()),
            ],
        ),
    ]
