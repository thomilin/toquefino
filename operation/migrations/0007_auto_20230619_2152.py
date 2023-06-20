# Generated by Django 3.2.5 on 2023-06-20 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0006_remove_product_invoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='invoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='operation.invoice', unique=True),
        ),
    ]