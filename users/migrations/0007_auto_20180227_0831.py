# Generated by Django 2.0.2 on 2018-02-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20180227_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='shift',
            field=models.IntegerField(help_text='Number between 1 and 25', null=True),
        ),
    ]
