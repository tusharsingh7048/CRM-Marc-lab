# Generated by Django 5.0.4 on 2024-05-01 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('contactno', models.EmailField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('emailaddress', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('regdate', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('userid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('usertype', models.CharField(max_length=30)),
            ],
        ),
    ]
