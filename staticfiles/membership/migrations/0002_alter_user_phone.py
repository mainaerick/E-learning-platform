# Generated by Django 4.0.2 on 2022-02-04 16:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '254712345678. Up to 12 digits allowed.", regex='(\\+254|^){1}[ ]?[7]{1}([0-3]{1}[0-9]{1})[ ]?[0-9]{3}[ ]?[0-9]{3}\\z')]),
        ),
    ]