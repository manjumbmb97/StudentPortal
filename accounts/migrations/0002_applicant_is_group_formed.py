# Generated by Django 2.0.6 on 2018-06-24 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='is_group_formed',
            field=models.BooleanField(default=False),
        ),
    ]
