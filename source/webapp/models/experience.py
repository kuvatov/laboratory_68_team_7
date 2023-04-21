from django.db import models


class Experience(models.Model):
    start_date = models.DateField(
        null=False,
        blank=False
    )
    dismissal_date = models.DateField(
        null=True,
        blank=True
    )
    is_current = models.BooleanField(
        null=True,
        blank=True
    )
    company_name = models.CharField(
        max_length=100,
        verbose_name='Фирма'
    )
    position = models.CharField(
        max_length=100,
        verbose_name='Должность'
    )
    responsibilities = models.CharField(
        max_length=500,
        verbose_name="Обязанности"
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
        return self.position

    class Meta:
        verbose_name = 'Опыт'
        verbose_name_plural = 'Опыт'
