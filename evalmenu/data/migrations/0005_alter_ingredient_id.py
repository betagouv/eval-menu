# Generated by Django 5.1.3 on 2024-12-02 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0004_alter_ingredient_id_ecobalyse"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingredient",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
