# Generated by Django 3.2.16 on 2023-09-05 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personalization', '0010_remove_images_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='ViewerDetail_ID',
        ),
        migrations.AddField(
            model_name='messages',
            name='Age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='messages',
            name='Gender',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]