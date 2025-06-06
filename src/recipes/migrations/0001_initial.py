# Generated by Django 5.2.1 on 2025-05-19 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='meals.meal')),
            ],
        ),
    ]
