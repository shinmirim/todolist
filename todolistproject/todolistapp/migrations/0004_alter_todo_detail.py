# Generated by Django 4.0.2 on 2022-02-11 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistapp', '0003_alter_todo_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='detail',
            field=models.CharField(max_length=255),
        ),
    ]