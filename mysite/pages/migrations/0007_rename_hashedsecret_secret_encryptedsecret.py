# Generated by Django 4.1.3 on 2022-12-18 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0006_alter_secret_secretkey"),
    ]

    operations = [
        migrations.RenameField(
            model_name="secret",
            old_name="hashedsecret",
            new_name="encryptedsecret",
        ),
    ]
