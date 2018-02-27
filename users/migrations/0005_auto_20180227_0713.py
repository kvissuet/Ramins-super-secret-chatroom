# Generated by Django 2.0.2 on 2018-02-27 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180227_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prime_1',
            field=models.IntegerField(help_text='First Favorite Prime'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='prime_2',
            field=models.IntegerField(help_text='Second Favorite Prime'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='shift',
            field=models.IntegerField(help_text='Number between 1 and 25'),
        ),
    ]