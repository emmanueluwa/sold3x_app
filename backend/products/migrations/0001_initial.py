# Generated by Django 4.0.4 on 2022-04-27 10:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.URLField(max_length=500)),
                ('url', models.URLField(max_length=500)),
                ('title', models.CharField(max_length=250)),
                ('condition', models.CharField(max_length=100)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('sold_time', models.DateTimeField()),
                ('listing_type', models.CharField(max_length=50)),
            ],
        ),
    ]
