# Generated by Django 4.0.2 on 2022-02-11 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistapp', '0004_alter_todo_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='detail',
            field=models.TextField(),
        ),
    ]
