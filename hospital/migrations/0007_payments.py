# Generated by Django 3.0.3 on 2020-09-23 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_auto_20200923_0408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_name', models.CharField(help_text='Enter the name for account', max_length=20)),
                ('Account_type', models.CharField(choices=[('M', 'Mastercard'), ('V', 'Visa')], help_text='Choose a type for the card', max_length=3)),
                ('Account_number', models.IntegerField()),
                ('Account_password', models.CharField(help_text='Enter the password', max_length=20)),
                ('Account_pin', models.SmallIntegerField()),
                ('Account_balance', models.IntegerField(help_text='The account balance')),
            ],
        ),
    ]
