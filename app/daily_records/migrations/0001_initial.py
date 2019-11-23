# Generated by Django 2.2.7 on 2019-11-23 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_fit', models.BooleanField(default=True, null=True)),
                ('date', models.DateField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
