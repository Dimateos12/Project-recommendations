# Generated by Django 4.1.2 on 2023-01-19 18:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("recommenders", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Candidate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=150, unique=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("invited", "Invited"), ("confirmed", "Confirmed")],
                        default="invited",
                        max_length=30,
                    ),
                ),
                (
                    "referrer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="recommenders.recommender",
                    ),
                ),
            ],
        ),
    ]
