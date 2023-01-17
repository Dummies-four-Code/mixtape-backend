# Generated by Django 4.0.5 on 2022-06-26 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0013_alter_mixtape_creator"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mixtape",
            name="creator",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mixtapes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]