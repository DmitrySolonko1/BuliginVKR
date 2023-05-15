# Generated by Django 4.2 on 2023-05-14 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpaApp', '0002_alter_masters_photo_alter_services_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masters',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='services',
            name='category',
        ),
        migrations.RemoveField(
            model_name='services',
            name='masters',
        ),
        migrations.AddField(
            model_name='masters',
            name='services',
            field=models.ManyToManyField(related_name='specialists', to='SpaApp.services'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]