# Generated by Django 4.2.13 on 2024-06-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_remove_user_is_student_remove_user_is_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
    ]
