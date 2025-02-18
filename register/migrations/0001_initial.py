# Generated by Django 3.1.4 on 2020-12-27 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=10, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('mobile', models.CharField(default=False, max_length=10, unique=True)),
                ('email', models.EmailField(default=False, max_length=254, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('phone_confirmed', models.BooleanField(default=False)),
            ],
        ),
    ]
