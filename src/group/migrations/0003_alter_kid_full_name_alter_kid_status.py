# Generated by Django 5.2.1 on 2025-05-24 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_alter_kid_age_alter_kid_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='full_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='kid',
            name='status',
            field=models.CharField(choices=[('active', 'Faol'), ('inactive', 'Nofaol')], max_length=10),
        ),
    ]
