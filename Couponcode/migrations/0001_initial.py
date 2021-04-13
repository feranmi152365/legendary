# Generated by Django 3.1.1 on 2021-04-08 17:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('valid_from', models.DateField()),
                ('valid_to', models.DateField()),
                ('package', models.IntegerField(validators=[django.core.validators.MinValueValidator(5000), django.core.validators.MaxValueValidator(100000)])),
                ('active', models.BooleanField()),
            ],
        ),
    ]
