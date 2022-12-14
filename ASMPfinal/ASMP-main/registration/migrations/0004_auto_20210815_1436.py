# Generated by Django 2.2.5 on 2021-08-15 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20210815_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='experience',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='goal',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='obstacle',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pref_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pref_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pref_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pref_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pref_5',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
