from django.db import models


class Education(models.Model):
    graduation_date = models.DateField(
        null=False,
        blank=False,
        verbose_name="Год окончания"
    )
    institution_name = models.CharField(
        max_length=100,
        verbose_name='Учебное заведение'
    )
    specialisation = models.CharField(
        max_length=100,
        verbose_name='Специализация'
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
        return self.institution_name

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'

