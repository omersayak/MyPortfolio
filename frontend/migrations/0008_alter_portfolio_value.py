# Generated by Django 4.2.4 on 2023-08-26 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_portfolio_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='value',
            field=models.CharField(max_length=255),
        ),
    ]
