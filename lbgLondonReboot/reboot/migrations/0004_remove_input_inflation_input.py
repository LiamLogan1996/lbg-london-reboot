# Generated by Django 3.1.1 on 2022-11-30 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reboot', '0003_auto_20221122_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='input',
            name='inflation_input',
        ),
    ]
