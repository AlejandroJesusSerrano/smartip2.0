# Generated by Django 4.1.3 on 2022-11-24 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appsmartip', '0002_remove_device_brand_model_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='dev_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appsmartip.devtype'),
            preserve_default=False,
        ),
    ]