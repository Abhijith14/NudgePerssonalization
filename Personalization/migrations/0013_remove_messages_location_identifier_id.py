# Generated by Django 3.2.16 on 2023-09-05 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Personalization', '0012_auto_20230905_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='Location_Identifier_ID',
        ),
    ]
