# Generated by Django 4.1.3 on 2022-12-18 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0007_rename_hashedsecret_secret_encryptedsecret"),
    ]

    operations = [
        migrations.AlterField(
            model_name="secret",
            name="user",
            field=models.TextField(unique=True),
        ),
    ]