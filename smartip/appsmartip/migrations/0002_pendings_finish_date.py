# Generated by Django 4.1.3 on 2023-02-10 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsmartip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pendings',
            name='finish_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Terminar para'),
        ),
    ]
