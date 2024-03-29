# Generated by Django 5.0.1 on 2024-01-26 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='city',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='country',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='state',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='street',
        ),
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.TextField(blank=True, default='', help_text='country, city, state, street,', max_length=1000),
        ),
    ]
