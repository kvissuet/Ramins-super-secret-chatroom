# Generated by Django 2.0.2 on 2018-02-27 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180227_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='RSA_n',
            field=models.IntegerField(help_text='Product of Primes', null=True),
        ),
    ]
