# Generated by Django 5.0.4 on 2024-05-22 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0003_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='Name',
            new_name='name',
        ),
    ]
