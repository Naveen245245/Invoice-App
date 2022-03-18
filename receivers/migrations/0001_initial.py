# Generated by Django 3.2.3 on 2022-03-09 01:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('website', models.URLField(blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('logo', models.ImageField(default='images/no_photo.png', upload_to='')),
            ],
        ),
    ]