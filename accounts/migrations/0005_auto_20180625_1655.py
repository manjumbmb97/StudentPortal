# Generated by Django 2.0.6 on 2018-06-25 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180625_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='course',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='duration',
            field=models.IntegerField(default=7),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='group_strength',
            field=models.IntegerField(default=1),
        ),
    ]