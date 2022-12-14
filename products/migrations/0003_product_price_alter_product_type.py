# Generated by Django 4.1.3 on 2022-12-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_buy_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=True, max_digits=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.SmallIntegerField(choices=[(1, 'bigger then 10 inch'), (2, 'smaller then 10 inch')], default=1),
        ),
    ]
