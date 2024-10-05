# Generated by Django 5.1 on 2024-09-17 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Base2',
            fields=[
                ('base1_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.base1')),
                ('age', models.IntegerField(default=20, null=True)),
                ('last_name', models.CharField(default=None, max_length=100, null=True)),
            ],
            bases=('api.base1',),
        ),
    ]