# Generated by Django 4.2.4 on 2023-08-27 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0021_delete_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortoflioTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('isActive', models.BooleanField(default=True)),
                ('menus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('projectTitle', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('projectType', models.CharField(max_length=255)),
                ('producer', models.TextField(max_length=255)),
                ('projectLink', models.TextField()),
                ('language', models.CharField(max_length=255)),
                ('isActive', models.BooleanField(default=True)),
                ('menus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.menu')),
            ],
        ),
    ]
