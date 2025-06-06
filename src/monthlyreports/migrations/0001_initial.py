# Generated by Django 5.2.1 on 2025-05-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyReports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_year', models.CharField(max_length=7)),
                ('total_served', models.IntegerField()),
                ('total_possible', models.IntegerField()),
                ('difference_percent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('generated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
