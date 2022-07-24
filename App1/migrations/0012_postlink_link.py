# Generated by Django 4.0.3 on 2022-07-20 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0011_commentsb_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.fromcomp')),
            ],
        ),
        migrations.CreateModel(
            name='link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='click here', max_length=30)),
                ('url', models.URLField(default='', max_length=999999999)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.postlink')),
            ],
        ),
    ]
