# Generated by Django 5.0.7 on 2024-07-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('linkedin', models.CharField(max_length=100)),
                ('github', models.CharField(max_length=100)),
                ('telegram', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
            ],
        ),
    ]
