# Generated by Django 5.1.1 on 2024-11-07 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_be', '0014_alter_contacts_user_delete_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='clients',
            field=models.ManyToManyField(blank=True, related_name='assigned_tasks', to='join_be.contacts'),
        ),
    ]
