# Generated by Django 2.2.3 on 2019-07-23 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20190723_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busdata',
            name='seats_left',
            field=models.IntegerField(),
        ),
    ]
