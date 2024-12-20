# Generated by Django 5.1.3 on 2024-12-03 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0008_alter_recette_cs_alter_recette_nutriscore"),
    ]

    operations = [
        migrations.AddField(
            model_name="recette",
            name="is_bio",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="recette",
            name="cs",
            field=models.IntegerField(
                blank=True, default=None, help_text="Score environnemental", null=True
            ),
        ),
        migrations.AlterField(
            model_name="recette",
            name="nutriscore",
            field=models.CharField(
                blank=True,
                choices=[("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"), ("E", "E")],
                default=None,
                max_length=1,
                null=True,
            ),
        ),
    ]
