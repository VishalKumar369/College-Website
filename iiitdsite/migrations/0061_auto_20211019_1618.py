# Generated by Django 3.2.6 on 2021-10-19 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iiitdsite', '0060_auto_20211017_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='BOG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('role', models.CharField(max_length=200, null=True)),
                ('tag', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='BOG/')),
            ],
        ),
        migrations.CreateModel(
            name='Financial_Committee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('role', models.CharField(max_length=200, null=True)),
                ('tag', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='FinanceCommittee/')),
            ],
        ),
        migrations.CreateModel(
            name='Senate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('role', models.CharField(max_length=200, null=True)),
                ('tag', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Senate/')),
            ],
        ),
        migrations.DeleteModel(
            name='BOGChairperson',
        ),
        migrations.DeleteModel(
            name='BOGMembers',
        ),
        migrations.DeleteModel(
            name='BOGNonMembers',
        ),
        migrations.DeleteModel(
            name='FinanceCommitteeMembers',
        ),
        migrations.DeleteModel(
            name='SenateChairperson',
        ),
        migrations.DeleteModel(
            name='SenateMembers',
        ),
    ]