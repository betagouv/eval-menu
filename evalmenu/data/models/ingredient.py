from django.db import models


class Ingredient(models.Model):
    id = models.IntegerField(primary_key=True)
    id_ecobalyse = models.CharField(max_length=40)
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name