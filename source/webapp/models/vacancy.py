from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Vacancy(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    salary = models.PositiveIntegerField(
        verbose_name='Заработная плата'
    )
    description = models.TextField(
        max_length=3000,
        blank=True,
        verbose_name='Описание'
    )
    experience_from = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Опыт работы (От)'
    )
    experience_to = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Опыт работы (До)'
    )
    category = models.ForeignKey(
        to='webapp.Category',
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )
    owner = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        default=1,
        related_name='vacancies'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время изменения"
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликован'
    )
    is_deleted = models.BooleanField(
        null=False,
        default=False,
        verbose_name="Удален"
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
        verbose_name="Дата и время удаления"
    )

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
