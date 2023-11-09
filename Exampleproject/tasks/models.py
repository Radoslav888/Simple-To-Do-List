from enum import Enum
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

# Create your models here.
UserModel = get_user_model()


class Task(models.Model):
    MIN_NAME_LENGTH = 3
    MAX_NAME_LENGTH = 50

    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 600

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_NAME_LENGTH),
        ),
        null=False,
        blank=False,
        verbose_name='Task'
    )
    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=False,
        blank=False,
    )

    status = models.BooleanField(

    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')

        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
