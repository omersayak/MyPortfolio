# Generated by Django 4.2.4 on 2023-08-27 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0018_footer'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='img',
            field=models.ImageField(blank=True, upload_to='uploads'),
        ),
    ]
