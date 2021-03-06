# Generated by Django 3.1.5 on 2021-01-13 05:28

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('phone', phone_field.models.PhoneField(max_length=31)),
                ('comment', models.TextField(max_length=400)),
                ('date', models.DateField()),
            ],
        ),
    ]
