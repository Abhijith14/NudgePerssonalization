# Generated by Django 3.2.16 on 2023-09-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personalization', '0006_alter_ftpaddress_ftp_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='Image_ID',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
