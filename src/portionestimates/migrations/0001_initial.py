# Generated by Django 5.2.1 on 2025-05-18 20:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortionEstimate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('possible_portions', models.IntegerField()),
                ('calculated_at', models.DateTimeField(auto_now_add=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portion_estimates', to='recipes.recipe')),
            ],
        ),
    ]
