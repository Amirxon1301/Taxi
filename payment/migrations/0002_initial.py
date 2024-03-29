# Generated by Django 5.0.1 on 2024-01-29 09:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('driver', '0002_initial'),
        ('payment', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.driver'),
        ),
        migrations.AddField(
            model_name='payment',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.operator'),
        ),
    ]
