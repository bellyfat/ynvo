# Generated by Django 2.1.7 on 2019-03-04 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ynvo', '0002_auto_20190303_0135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='status',
        ),
        migrations.AddField(
            model_name='invoice',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='paid',
            field=models.DateField(blank=True, null=True),
        ),
    ]