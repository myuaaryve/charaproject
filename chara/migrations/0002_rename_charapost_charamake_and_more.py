# Generated by Django 4.1 on 2023-11-26 10:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chara", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CharaPost",
            new_name="CharaMake",
        ),
        migrations.RenameField(
            model_name="charamake",
            old_name="Category",
            new_name="category",
        ),
    ]