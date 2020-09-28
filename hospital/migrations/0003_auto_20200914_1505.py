# Generated by Django 3.0.3 on 2020-09-14 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20200914_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], help_text='Enter gender', max_length=2),
        ),
    ]
