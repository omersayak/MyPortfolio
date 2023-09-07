# Generated by Django 4.2.4 on 2023-08-25 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter', models.CharField(max_length=100)),
                ('value', models.TextField()),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('skillValue', models.SmallIntegerField()),
                ('skillName', models.CharField(max_length=255)),
                ('isActive', models.BooleanField(default=True)),
                ('menus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('value', models.TextField(blank=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('menus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='uploads')),
                ('projectType', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=255)),
                ('task', models.CharField(max_length=255)),
                ('isActive', models.BooleanField(default=True)),
                ('menus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.menu')),
            ],
        ),
        migrations.CreateModel(
            name='IntroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('isActive', models.BooleanField(default=True)),
                ('menus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('value', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField()),
                ('isActive', models.BooleanField(default=True)),
                ('menus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('address', models.TextField()),
                ('isActive', models.BooleanField(default=True)),
                ('menus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('menus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.menu')),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('value', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('age', models.IntegerField()),
                ('education', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('freelance', models.CharField(max_length=255)),
                ('isActive', models.BooleanField(default=True)),
                ('menus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.menu')),
            ],
        ),
    ]
