# Generated by Django 3.2.25 on 2025-05-29 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0008_auto_20250527_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='complaints_text',
            field=models.TextField(null=True, verbose_name='Текст жалобы'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='property.flat', verbose_name='Квартира на которую пожаловались'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('owners_phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('owner_pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='RU', verbose_name='Нормализованный номер владельца')),
                ('flats', models.ManyToManyField(related_name='owner_flats', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
