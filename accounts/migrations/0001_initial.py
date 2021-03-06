# Generated by Django 2.0.6 on 2018-06-24 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('portal', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.IntegerField(default=0)),
                ('internship_type', models.CharField(choices=[('T', 'Training'), ('P', 'Project')], default='T', max_length=1)),
                ('duration', models.IntegerField(default=7, null=True)),
                ('course', models.CharField(max_length=250, null=True)),
                ('department', models.CharField(choices=[('CS', 'Computer Science Engineering'), ('CV', 'Civil Engineering'), ('CH', 'Chemical Engineering'), ('EC', 'Electronics Engineering'), ('EE', 'Electrical Engineering'), ('ME', 'Mechanical Engineering'), ('MT', 'Metallurgical Engineering'), ('MN', 'Mining Engineering')], default='CS', max_length=2)),
                ('group_strength', models.IntegerField(default=1, null=True)),
                ('reporting_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_filled', models.BooleanField(default=False)),
                ('slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Slot')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Official',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.IntegerField(default=0)),
                ('employee_id', models.CharField(default='', max_length=10)),
                ('designation', models.CharField(default='', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
