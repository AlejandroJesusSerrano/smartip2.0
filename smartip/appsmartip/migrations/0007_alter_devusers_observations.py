<<<<<<< HEAD
# Generated by Django 4.1.3 on 2023-02-09 13:54
=======
# Generated by Django 4.1.3 on 2023-02-09 14:52
>>>>>>> 0f1514f22a5eab7fb0b036600b0c658f7529d317

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsmartip', '0006_alter_pendings_options_pendings_office'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devusers',
            name='observations',
            field=models.TextField(blank=True, null=True),
        ),
    ]
