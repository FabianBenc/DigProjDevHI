# Generated by Django 4.2 on 2023-06-06 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blockaid', '0004_color_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='color',
            old_name='user_id',
            new_name='user',
        ),
    ]
