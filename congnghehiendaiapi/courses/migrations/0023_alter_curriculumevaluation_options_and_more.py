# Generated by Django 4.2.13 on 2024-06-18 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0022_alter_user_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curriculumevaluation',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='curriculumevaluation',
            unique_together={('curriculum', 'evaluation_criterion')},
        ),
    ]
