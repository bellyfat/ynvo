# Generated by Django 2.2.1 on 2019-07-12 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ynvo', '0005_auto_20190402_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='currency_exchange',
            field=models.FloatField(default=1.0),
        ),
        migrations.AddField(
            model_name='invoice',
            name='extra_currency',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]