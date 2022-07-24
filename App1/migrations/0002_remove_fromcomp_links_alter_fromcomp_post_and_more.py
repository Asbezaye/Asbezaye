# Generated by Django 4.0.3 on 2022-07-16 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fromcomp',
            name='links',
        ),
        migrations.AlterField(
            model_name='fromcomp',
            name='post',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='serial',
            name='code',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='useron',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='useron',
            name='serial',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='App1.serial'),
        ),
    ]
