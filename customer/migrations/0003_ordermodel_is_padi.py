# Generated by Django 3.1.4 on 2020-12-25 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20201225_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_padi',
            field=models.BooleanField(default=False),
        ),
    ]
