# Generated by Django 3.0.6 on 2020-06-04 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0011_auto_20200604_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_exam',
            name='is_started',
            field=models.BooleanField(default=False),
        ),
    ]