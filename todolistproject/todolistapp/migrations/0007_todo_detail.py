# Generated by Django 4.0.2 on 2022-02-11 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistapp', '0006_remove_todo_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='detail',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
