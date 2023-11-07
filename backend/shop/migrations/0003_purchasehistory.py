# Generated by Django 4.1.2 on 2023-06-02 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recommenders", "0001_initial"),
        ("shop", "0002_alter_image_image_alter_image_reward"),
    ]

    operations = [
        migrations.CreateModel(
            name="PurchaseHistory",
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
                (
                    "purchase_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="purchase date"
                    ),
                ),
                (
                    "points_spent",
                    models.PositiveIntegerField(verbose_name="points spent"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("ORDERED", "Ordered"),
                            ("SENT", "Sent"),
                            ("RECEIVED", "Received"),
                        ],
                        default="ORDERED",
                        max_length=8,
                        verbose_name="status",
                    ),
                ),
                (
                    "shipping_address",
                    models.TextField(
                        blank=True, null=True, verbose_name="shipping address"
                    ),
                ),
                (
                    "recommender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recommender_purchase_histories",
                        to="recommenders.recommender",
                        verbose_name="recommender",
                    ),
                ),
                (
                    "reward",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="purchase_history_reward",
                        to="shop.reward",
                        verbose_name="reward",
                    ),
                ),
            ],
            options={
                "verbose_name": "Purchase history",
                "verbose_name_plural": "Purchase histories",
            },
        ),
    ]
