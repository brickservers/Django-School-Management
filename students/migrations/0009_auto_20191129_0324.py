# Generated by Django 2.2.7 on 2019-11-28 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20191129_0322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['roll', 'registration_number']},
        ),
    ]
