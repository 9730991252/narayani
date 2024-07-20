# Generated by Django 5.0.7 on 2024-07-20 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_select_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
        migrations.AddField(
            model_name='product',
            name='courier_charges_maharashtra',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='courier_charges_other_states',
            field=models.FloatField(default=0),
        ),
    ]
