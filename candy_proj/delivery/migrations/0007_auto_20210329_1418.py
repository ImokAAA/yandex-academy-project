# Generated by Django 3.1.7 on 2021-03-29 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0006_auto_20210326_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='courier_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='delivery.courier'),
        ),
    ]