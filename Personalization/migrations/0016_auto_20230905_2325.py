# Generated by Django 3.2.16 on 2023-09-05 22:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Personalization', '0015_auto_20230905_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='Age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='Course',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='Date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='messages',
            name='Gender',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='Nationality',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='Time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]