# Generated by Django 2.0.2 on 2022-08-09 09:35

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
            name='ASMPProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=6)),
                ('sop', models.CharField(blank=True, max_length=500)),
                ('linkedin', models.CharField(blank=True, max_length=100)),
                ('pref_1', models.IntegerField(blank=True, null=True)),
                ('pref_2', models.IntegerField(blank=True, null=True)),
                ('pref_3', models.IntegerField(blank=True, null=True)),
                ('pref_4', models.IntegerField(blank=True, null=True)),
                ('pref_5', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('gender', models.CharField(default='Male', max_length=10)),
                ('year', models.CharField(default='2018', max_length=20)),
                ('department', models.CharField(default='Civil', max_length=100)),
                ('degree', models.CharField(default='BTech', max_length=100)),
                ('city', models.CharField(default='Mumbai', max_length=100)),
                ('country', models.CharField(default='India', max_length=100)),
                ('designation', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('discp', models.TextField(blank=True)),
                ('interest', models.CharField(max_length=200, null=True)),
                ('maxmentees', models.IntegerField(default=0)),
                ('score', models.FloatField(default=0.0)),
                ('available', models.BooleanField(default=True)),
                ('maxscore', models.FloatField(default=0.0)),
                ('favourites', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
