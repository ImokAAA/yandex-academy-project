# Generated by Django 3.1.7 on 2021-03-26 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0004_deliveryhour_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliveryhour',
            old_name='courier_id',
            new_name='order_id',
        ),
        migrations.AddField(
            model_name='order',
            name='assign_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='complete_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='courier_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.courier'),
        ),
    ]