# Generated by Django 4.1.2 on 2022-11-19 18:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompanyAdmin",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("company", models.CharField(max_length=150)),
            ],
            options={
                "verbose_name": "CompanyAdmin",
                "verbose_name_plural": "CompanyAdmins",
            },
            bases=("users.user",),
            managers=[
                ("objects", users.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Advertisment",
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
                ("title", models.CharField(max_length=150)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("COMMERCIAL", "Commercial"),
                            ("RECRUITMENT", "Recruitment"),
                        ],
                        max_length=11,
                    ),
                ),
                ("reward_for_approval", models.PositiveIntegerField()),
                (
                    "company",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="companies.companyadmin",
                    ),
                ),
            ],
            options={
                "verbose_name": "Advertisment",
                "verbose_name_plural": "Advertisments",
            },
        ),
    ]
