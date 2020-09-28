# Generated by Django 3.0.3 on 2020-09-23 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_payments'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='user-images'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='venue',
            field=models.CharField(choices=[('A', 'Hospital'), ('B', 'Home'), ('C', 'Online')], default='H', help_text='The venue for appointment', max_length=2),
        ),
    ]