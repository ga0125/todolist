# Generated by Django 2.2.5 on 2019-09-08 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0002_todo_completed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]