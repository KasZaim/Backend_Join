# Generated by Django 5.1.1 on 2024-10-04 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_be', '0006_alter_tasks_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='subtask',
        ),
        migrations.AddField(
            model_name='tasks',
            name='subtasks',
            field=models.JSONField(blank=True, default=list, help_text='status: toDo, inProgress, awaitingFeedback, done', null=True),
        ),
    ]
