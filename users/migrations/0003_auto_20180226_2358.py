# Generated by Django 2.0.2 on 2018-02-27 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_shift'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='prime_1',
            field=models.CharField(default=1, help_text='First Favorite Prime', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='prime_2',
            field=models.CharField(default=1, help_text='Second Favorite Prime', max_length=20),
            preserve_default=False,
        ),
    ]
