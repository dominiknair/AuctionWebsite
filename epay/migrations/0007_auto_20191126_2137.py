# Generated by Django 2.2.6 on 2019-11-26 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epay', '0006_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='item',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='epay.Item'),
        ),
    ]
