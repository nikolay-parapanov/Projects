# Generated by Django 4.1.4 on 2022-12-11 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authh', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]