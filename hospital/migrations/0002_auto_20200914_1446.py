# Generated by Django 3.0.3 on 2020-09-14 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text='Enter the date of birth', null=True),
        ),
    ]
