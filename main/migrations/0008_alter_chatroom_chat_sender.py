# Generated by Django 5.1.5 on 2025-01-25 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_chatroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='chat_sender',
            field=models.CharField(max_length=250),
        ),
    ]