# Generated by Django 4.2 on 2023-04-17 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0004_alter_vacancy_owner"),
    ]

    operations = [
        migrations.RemoveField(model_name="vacancy", name="deleted_at",),
        migrations.RemoveField(model_name="vacancy", name="is_deleted",),
    ]
