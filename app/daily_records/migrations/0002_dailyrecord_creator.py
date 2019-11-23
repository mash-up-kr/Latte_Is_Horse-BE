# Generated by Django 2.2.7 on 2019-11-23 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('daily_records', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyrecord',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='daliy_records', to=settings.AUTH_USER_MODEL),
        ),
    ]
