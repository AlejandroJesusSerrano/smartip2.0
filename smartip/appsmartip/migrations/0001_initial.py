# Generated by Django 4.1.3 on 2022-12-01 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('court', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_name', models.CharField(max_length=10)),
                ('is_active', models.BooleanField()),
                ('is_working', models.BooleanField()),
                ('last_revision', models.DateField()),
                ('cause', models.CharField(max_length=50)),
                ('has_user', models.BooleanField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsmartip.brand')),
            ],
        ),
        migrations.CreateModel(
            name='DevStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='DevType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_type', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='DevUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=60)),
                ('message_acount', models.CharField(max_length=15)),
                ('message_pass', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=6)),
                ('standard_password', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Edifice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edifice', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Internet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_type', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='devices')),
                ('model', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PendingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=19)),
            ],
        ),
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pendings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('personal', models.BooleanField()),
                ('reason', models.TextField()),
                ('updated', models.DateField(auto_now=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsmartip.device')),
                ('required_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_require', to='appsmartip.devusers')),
                ('service_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_for', to='appsmartip.devusers')),
                ('state', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appsmartip.pendingstatus')),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.CharField(max_length=4)),
                ('office_name', models.CharField(max_length=25)),
                ('phone_1', models.IntegerField(null=True)),
                ('phone_2', models.IntegerField(null=True)),
                ('phone_3', models.IntegerField(null=True)),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsmartip.court')),
                ('edifice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsmartip.edifice')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsmartip.location')),
            ],
        ),
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipdir', models.CharField(max_length=15)),
                ('internet_access', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsmartip.internet')),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='dev_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsmartip.devtype'),
        ),
        migrations.AddField(
            model_name='device',
            name='ip_direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsmartip.ip'),
        ),
        migrations.AddField(
            model_name='device',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsmartip.model'),
        ),
        migrations.AddField(
            model_name='device',
            name='office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsmartip.office'),
        ),
        migrations.AddField(
            model_name='device',
            name='tech_revision',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsmartip.tech'),
        ),
        migrations.AddField(
            model_name='device',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsmartip.devusers'),
        ),
        migrations.CreateModel(
            name='AssignedTech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assign_date', models.DateTimeField(auto_now_add=True)),
                ('finished', models.BooleanField()),
                ('date', models.DateField()),
                ('observations', models.TextField()),
                ('repair', models.CharField(max_length=50)),
                ('updated', models.DateField(auto_now=True)),
                ('pending', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsmartip.pendings')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsmartip.pendingstatus')),
                ('tech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsmartip.tech')),
            ],
        ),
    ]
