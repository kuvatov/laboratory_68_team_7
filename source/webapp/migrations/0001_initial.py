# Generated by Django 4.2 on 2023-04-16 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Категория")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата и время изменения"
                    ),
                ),
            ],
            options={"verbose_name_plural": "Категории",},
        ),
        migrations.CreateModel(
            name="Vacancy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "salary",
                    models.PositiveIntegerField(verbose_name="Заработная плата"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=3000, verbose_name="Описание"
                    ),
                ),
                (
                    "experience_from",
                    models.PositiveIntegerField(verbose_name="Опыт работы (От)"),
                ),
                (
                    "experience_to",
                    models.PositiveIntegerField(verbose_name="Опыт работы (До)"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата и время изменения"
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(default=False, verbose_name="Опубликован"),
                ),
                (
                    "is_deleted",
                    models.BooleanField(default=False, verbose_name="Удален"),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        default=None, null=True, verbose_name="Дата и время удаления"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="webapp.category",
                        verbose_name="Категория",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vacancies",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"verbose_name": "Вакансия", "verbose_name_plural": "Вакансии",},
        ),
    ]