# Generated by Django 5.0.6 on 2025-05-22 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_order_alter_userlogin_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='image',
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(max_length=20),
        ),
    ]
