# Generated by Django 3.2.2 on 2022-09-19 12:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groc_item', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('item_pprice', models.DecimalField(decimal_places=2, max_digits=8)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Items',
                'ordering': ['groc_item'],
            },
        ),
    ]
