# Generated by Django 4.2.4 on 2023-08-26 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0011_service_serviceicon'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blogTitle',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='BlogTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('isActive', models.BooleanField(default=True)),
                ('menus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.menu')),
            ],
        ),
    ]
