# Generated by Django 4.2.13 on 2024-05-29 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_remove_syllabus_curriculums_syllabus_curriculum'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluationcriterion',
            name='curriculum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.curriculum'),
        ),
    ]
