# Generated by Django 5.0.6 on 2024-05-09 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phase', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('phase', models.IntegerField()),
                ('type', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=255)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtb_v4_app.page')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('phase', models.IntegerField()),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtb_v4_app.page')),
            ],
        ),
    ]