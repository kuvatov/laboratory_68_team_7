# Generated by Django 4.2 on 2023-04-16 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vacancy",
            name="deleted_at",
            field=models.DateTimeField(
                blank=True,
                default=None,
                null=True,
                verbose_name="Дата и время удаления",
            ),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="experience_from",
            field=models.PositiveIntegerField(
                blank=True, verbose_name="Опыт работы (От)"
            ),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="experience_to",
            field=models.PositiveIntegerField(
                blank=True, verbose_name="Опыт работы (До)"
            ),
        ),
    ]