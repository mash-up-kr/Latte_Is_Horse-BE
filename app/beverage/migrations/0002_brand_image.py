# Generated by Django 2.2.7 on 2019-11-23 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beverage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(null=True, upload_to='brand'),
        ),
    ]
