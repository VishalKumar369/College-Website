# Generated by Django 3.0.8 on 2020-09-12 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iiitdsite', '0016_jobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_link', models.CharField(max_length=200)),
            ],
        ),
    ]