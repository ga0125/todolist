# Generated by Django 2.2.5 on 2019-09-09 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0004_auto_20190908_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
