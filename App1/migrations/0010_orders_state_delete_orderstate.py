# Generated by Django 4.0.3 on 2022-07-18 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0009_alter_orders_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='state',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='OrderState',
        ),
    ]