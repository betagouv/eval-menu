# Generated by Django 5.1.3 on 2024-12-02 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_recette_cs_recette_nutriscore_recette_type_plat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recette',
            name='cs',
            field=models.IntegerField(help_text='Score environnemental', null=True),
        ),
    ]
