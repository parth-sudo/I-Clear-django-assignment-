# Generated by Django 3.2.2 on 2021-09-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP', models.CharField(max_length=17)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
