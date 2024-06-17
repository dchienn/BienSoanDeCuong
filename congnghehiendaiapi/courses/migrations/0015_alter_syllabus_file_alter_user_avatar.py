# Generated by Django 5.0.6 on 2024-06-13 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syllabus',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='syllabus/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/avatar/%Y/%m/%d/'),
        ),
    ]
