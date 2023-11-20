# Generated by Django 4.1.2 on 2023-11-20 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0014_topsissolusi"),
    ]

    operations = [
        migrations.CreateModel(
            name="JarakPrefTopsis",
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
                ("positif", models.FloatField(blank=True, default=0, null=True)),
                ("negatif", models.FloatField(blank=True, default=0, null=True)),
                ("preferensi", models.FloatField(blank=True, default=0, null=True)),
                (
                    "nimAlter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mysite.alternatif",
                        to_field="nimA",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Jarak-Pref-Topsis",
            },
        ),
    ]
