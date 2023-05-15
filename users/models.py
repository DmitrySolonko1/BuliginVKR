from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    name = models.CharField(max_length=100, verbose_name="Имя")
    middlename = models.CharField(max_length=100, verbose_name="Отчество", blank=True)
    email = models.EmailField(max_length=221, verbose_name="email")
    phone = models.CharField(max_length=12, verbose_name="Номер телефона", unique=True)
    status = models.BooleanField(default=False, verbose_name='Подтверждение аккаунта')

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
