# Generated by Django 2.1.1 on 2018-09-21 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(default='', max_length=20)),
                ('matricula', models.IntegerField(default=0)),
                ('cr', models.CharField(default='', max_length=10)),
                ('nome', models.CharField(default='', max_length=60)),
                ('cpf', models.CharField(default='', max_length=13)),
                ('empresa', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(default='', max_length=75)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
