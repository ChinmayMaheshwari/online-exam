# Generated by Django 3.0.2 on 2020-06-01 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_section_no_of_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='negative_marks',
            field=models.IntegerField(default=0),
        ),
    ]
