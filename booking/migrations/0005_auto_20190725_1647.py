# Generated by Django 2.2.3 on 2019-07-25 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20190725_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booked',
            name='route_id',
        ),
        migrations.AddField(
            model_name='booked',
            name='str_route',
            field=models.CharField(default='jjj', max_length=100),
            preserve_default=False,
        ),
    ]
