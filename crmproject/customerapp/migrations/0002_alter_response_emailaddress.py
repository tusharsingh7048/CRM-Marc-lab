# Generated by Django 5.0.4 on 2024-05-17 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='emailaddress',
            field=models.EmailField(max_length=50),
        ),
    ]