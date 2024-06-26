# Generated by Django 3.2.12 on 2024-06-17 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('course', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('national_id', models.PositiveBigIntegerField()),
                ('teacher_department', models.CharField(max_length=25)),
            ],
        ),
    ]
