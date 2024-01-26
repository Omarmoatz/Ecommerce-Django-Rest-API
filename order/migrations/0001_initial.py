# Generated by Django 5.0.1 on 2024-01-26 19:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0005_review'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=50)),
                ('country', models.CharField(blank=True, default='', max_length=400)),
                ('city', models.CharField(blank=True, default='', max_length=400)),
                ('state', models.CharField(blank=True, default='', max_length=400)),
                ('street', models.CharField(blank=True, default='', max_length=500)),
                ('phone_num', models.PositiveIntegerField(blank=True, default=0)),
                ('status', models.CharField(blank=True, choices=[('Processing', 'Processing'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], max_length=50)),
                ('total_amount', models.PositiveIntegerField(blank=True, default=0)),
                ('payment_status', models.CharField(blank=True, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], max_length=50)),
                ('payment_mode', models.CharField(blank=True, choices=[('COD', 'COD'), ('Card', 'Card')], max_length=400)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_order', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrdersDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='order.orders')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_order', to='product.product')),
            ],
        ),
    ]
