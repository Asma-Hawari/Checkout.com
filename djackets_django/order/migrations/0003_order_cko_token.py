# Generated by Django 5.0.6 on 2024-07-05 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_checkoutpaymentid_order_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cko_token',
            field=models.CharField(max_length=100, null=True),
        ),
    ]