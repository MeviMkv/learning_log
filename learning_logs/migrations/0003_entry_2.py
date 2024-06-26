# Generated by Django 5.0.4 on 2024-04-11 00:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('Entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_logs.entry')),
            ],
            options={
                'verbose_name_plural': 'entries 2',
            },
        ),
    ]
