# Generated by Django 3.2.25 on 2024-06-06 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=50)),
                ('soyad', models.CharField(max_length=50)),
                ('ataadi', models.CharField(max_length=50)),
                ('yas', models.IntegerField()),
                ('tel', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('unvan', models.CharField(max_length=150)),
                ('tehsil', models.CharField(max_length=50)),
                ('isyeri', models.CharField(max_length=50)),
                ('vezife', models.CharField(max_length=50)),
            ],
        ),
    ]
