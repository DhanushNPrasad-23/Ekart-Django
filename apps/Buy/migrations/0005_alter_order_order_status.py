# Generated by Django 5.1 on 2024-09-14 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buy', '0004_remove_buy_order_status_order_order_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(blank=True, choices=[('', 'Select the catagaroies'), ('P', 'Pending'), ('C', 'Completed'), ('F', 'Failed')], default='P', max_length=10, null=True),
        ),
    ]