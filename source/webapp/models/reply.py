from django.contrib.auth import get_user_model
from django.db import models


class Reply(models.Model):
    vacancy = models.ForeignKey(
        to='webapp.Vacancy',
        on_delete=models.CASCADE,
        related_name='replies',
        verbose_name='Вакансия'
    )
    cv = models.ForeignKey(
        to='webapp.CV',
        on_delete=models.CASCADE,
        related_name='replies',
        verbose_name='Резюме'
    )
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name='replies',
        verbose_name='Пользователь'
    )
    message = models.TextField(
        blank=True,
        verbose_name='Сообщение'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время изменения"
    )

    def __str__(self):
        return f'{self.vacancy} - {self.user}'
