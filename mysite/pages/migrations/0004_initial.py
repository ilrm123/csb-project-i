# Generated by Django 4.1.3 on 2022-12-17 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("pages", "0003_delete_secret"),
    ]

    operations = [
        migrations.CreateModel(
            name="Secret",
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
                ("rawsecret", models.TextField()),
                ("hashedsecret", models.TextField()),
                ("writer", models.TextField()),
                ("secretkey", models.TextField()),
            ],
        ),
    ]
