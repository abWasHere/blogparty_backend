# Generated by Django 3.1.6 on 2021-02-17 16:48

from django.db import migrations


def create_venue_data(apps, schema_editor):
    Venue = apps.get_model("party", "Venue")
    Venue(
        name="Django Stadium", city="Paris", zip_code="75000", capacity=10000
    ).save()


class Migration(migrations.Migration):

    dependencies = [
        ("party", "0004_merge_20210217_1352"),
    ]

    operations = [
        migrations.RunPython(create_venue_data),
    ]
