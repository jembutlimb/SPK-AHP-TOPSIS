# Generated by Django 4.1.2 on 2023-11-14 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0003_alter_subkriteria_k1_alter_subkriteria_k2_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subkriteria",
            name="k1",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="subkriteria",
            name="k2",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="subkriteria",
            name="k3",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="subkriteria",
            name="k4",
            field=models.TextField(blank=True, null=True),
        ),
    ]
