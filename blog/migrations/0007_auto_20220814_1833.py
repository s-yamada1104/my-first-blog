# Generated by Django 3.2.15 on 2022-08-14 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20220814_1709'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sell',
            unique_together={('payment_id', 'product_id')},
        ),
        migrations.AlterModelTable(
            name='sell',
            table='blog_sell',
        ),
    ]
