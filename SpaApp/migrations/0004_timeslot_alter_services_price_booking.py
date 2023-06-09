# Generated by Django 4.2 on 2023-05-20 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SpaApp', '0003_remove_masters_categories_remove_services_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата и время бронирования')),
                ('is_available', models.BooleanField(default=True, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Время бронирования',
                'verbose_name_plural': 'Время бронирования',
            },
        ),
        migrations.AlterField(
            model_name='services',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255, verbose_name='Клиент')),
                ('masters', models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, to='SpaApp.masters', verbose_name='Риелтор')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SpaApp.services', verbose_name='Услуга для бронирования')),
                ('time_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SpaApp.timeslot', verbose_name='Время бронирования')),
            ],
            options={
                'verbose_name': 'Бронь',
                'verbose_name_plural': 'Бронь',
            },
        ),
    ]
