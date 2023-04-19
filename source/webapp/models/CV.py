from django.contrib.auth import get_user_model
from django.db import models


class CV(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название резюме (должность)'
    )
    category = models.ForeignKey(
        to='webapp.Category',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
    )
    owner = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        default=1,
        related_name='CVs'
    )
    experience = models.ManyToManyField(
        to='webapp.Experience',
        related_name='CVs',
    )
    education = models.ManyToManyField(
        to='webapp.Education',
        related_name='CVs'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время изменения")

    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
