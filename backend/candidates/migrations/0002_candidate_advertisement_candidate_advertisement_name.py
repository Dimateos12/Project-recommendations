# Generated by Django 4.1.2 on 2023-01-24 12:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0001_initial"),
        ("candidates", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidate",
            name="advertisement",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="candidate_advertisement",
                to="companies.advertisement",
                verbose_name="advertisement",
            ),
        ),
        migrations.AddField(
            model_name="candidate",
            name="advertisement_name",
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
