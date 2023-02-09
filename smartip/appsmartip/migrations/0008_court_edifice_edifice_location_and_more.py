# Generated by Django 4.1.3 on 2023-02-09 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appsmartip', '0007_alter_devusers_observations'),
    ]

    operations = [
        migrations.AddField(
            model_name='court',
            name='edifice',
            field=models.ForeignKey(default='SALTA CAPITAL', on_delete=django.db.models.deletion.CASCADE, to='appsmartip.edifice'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='edifice',
            name='location',
            field=models.ForeignKey(default='MONUMENTO A GUEMES', on_delete=django.db.models.deletion.CASCADE, to='appsmartip.location'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(max_length=14),
        ),
    ]