# Generated by Django 3.1.1 on 2022-11-17 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reboot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('salary_input', models.IntegerField(default=0)),
                ('inflation_input', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Inflation',
        ),
        migrations.DeleteModel(
            name='Salary',
        ),
    ]
