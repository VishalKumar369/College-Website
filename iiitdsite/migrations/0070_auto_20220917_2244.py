# Generated by Django 3.2.6 on 2022-09-17 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iiitdsite', '0069_auto_20220917_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='tag',
        ),
        migrations.AddField(
            model_name='images',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='iiitdsite.gallery_categories'),
        ),
    ]