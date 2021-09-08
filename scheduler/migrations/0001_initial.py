# Generated by Django 3.2.2 on 2021-09-08 07:49

from django.db import migrations, models
import scheduler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('unique_id', models.CharField(default=scheduler.models.random_code, max_length=6, unique=True)),
                ('image', models.ImageField(default='orange.jpg', upload_to='profile_pics')),
            ],
        ),
    ]
