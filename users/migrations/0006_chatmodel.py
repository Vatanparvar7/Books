# Generated by Django 3.1.14 on 2022-02-09 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220208_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.CharField(max_length=350)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('friend_chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_chat', to=settings.AUTH_USER_MODEL)),
                ('my_chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_chat', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
