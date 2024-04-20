# Generated by Django 5.0.4 on 2024-04-19 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_scapper_app', '0002_alter_cryptocurrency_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='change_1h',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='change_24h',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='change_7d',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='circulating_supply',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='market_cap',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='volume_24h',
            field=models.CharField(max_length=100),
        ),
    ]