# Generated by Django 5.0 on 2024-01-09 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_rename_id_message_msg_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='msg_id',
            new_name='id',
        ),
    ]