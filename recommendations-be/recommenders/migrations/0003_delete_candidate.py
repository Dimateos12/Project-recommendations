# Generated by Django 4.1.2 on 2023-01-13 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recommenders", "0002_remove_recommender_address"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Candidate",
        ),
    ]