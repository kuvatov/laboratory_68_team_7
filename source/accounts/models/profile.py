from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(
        to=get_user_model(),
        related_name="profile",
        on_delete=models.CASCADE,
        verbose_name="User profile"
    )

    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to="profile_picture"
    )
    is_corporate = models.BooleanField(
        null=True,
        blank=True,
    )
    phone_number = PhoneNumberField(
        blank=False,
        null=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
