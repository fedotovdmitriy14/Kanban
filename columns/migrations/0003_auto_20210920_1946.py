# Generated by Django 3.2.7 on 2021-09-20 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('columns', '0002_auto_20210920_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='date_time_field',
            field=models.DateTimeField(choices=[('datetime', (('true', 'required'), ('false', 'not required')))]),
        ),
        migrations.AlterField(
            model_name='column',
            name='integer_field',
            field=models.IntegerField(choices=[('integer', (('true', 'required'), ('false', 'not required')))]),
        ),
        migrations.AlterField(
            model_name='column',
            name='textarea_field',
            field=models.TextField(choices=[('textarea', (('true', 'required'), ('false', 'not required')))]),
        ),
    ]
