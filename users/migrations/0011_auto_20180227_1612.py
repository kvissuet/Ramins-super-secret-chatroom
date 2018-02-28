# Generated by Django 2.0.2 on 2018-02-27 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_userkeys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userkeys',
            name='RSA_n',
            field=models.IntegerField(help_text='Product of primes', null=True),
        ),
        migrations.AlterField(
            model_name='userkeys',
            name='RSA_private_key',
            field=models.IntegerField(help_text='Private Key', null=True),
        ),
        migrations.AlterField(
            model_name='userkeys',
            name='RSA_public_key',
            field=models.IntegerField(help_text='Public Key', null=True),
        ),
    ]