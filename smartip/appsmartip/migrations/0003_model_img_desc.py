# Generated by Django 4.1.3 on 2023-02-02 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsmartip', '0002_rename_message_acount_devusers_message_account_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='img_desc',
            field=models.CharField(default='image model', max_length=50),
            preserve_default=False,
        ),
    ]