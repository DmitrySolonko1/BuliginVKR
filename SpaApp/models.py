from django.db import models
from django.urls import reverse


class Masters(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    name = models.CharField(max_length=100, verbose_name="Имя")
    middlename = models.CharField(max_length=100, verbose_name="Отчество", blank=True)
    FIO = models.CharField(max_length=255, verbose_name='ФИО')
    services = models.ManyToManyField('Services', related_name='specialists')

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'


class Services(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    title = models.CharField(max_length=150, verbose_name='Название услуги')
    description = models.TextField(verbose_name='Описание услуги')
    duration = models.CharField(max_length=150, verbose_name='Длительность услуги')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def get_absolute_url(self):
        return reverse("service_detail", kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        super(Services, self).save(*args, **kwargs)


class TimeSlot(models.Model):
    time = models.DateTimeField(verbose_name='Дата и время бронирования')
    is_available = models.BooleanField(default=True, verbose_name='Статус')

    def __str__(self):
        return str(self.time)

    class Meta:
        verbose_name = 'Время бронирования'
        verbose_name_plural = 'Время бронирования'


class Booking(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Услуга для бронирования')
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, verbose_name='Время бронирования')
    client_name = models.CharField(max_length=255, verbose_name='Клиент')
    masters = models.ForeignKey(Masters, on_delete=models.CASCADE, verbose_name='Мастер')

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Бронь'