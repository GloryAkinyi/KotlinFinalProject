# Generated by Django 5.1.3 on 2024-11-19 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='passward',
            new_name='password',
        ),
    ]
