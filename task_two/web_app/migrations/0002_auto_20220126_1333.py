# Generated by Django 3.2.11 on 2022-01-26 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reliance',
            name='deliverable_qauntity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='reliance',
            name='no_of_shares',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='reliance',
            name='no_of_trades',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='reliance',
            name='total_turn_over',
            field=models.FloatField(),
        ),
    ]
