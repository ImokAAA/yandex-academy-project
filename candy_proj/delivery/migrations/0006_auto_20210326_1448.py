# Generated by Django 3.1.7 on 2021-03-26 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_auto_20210326_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='assign_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='complete_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
