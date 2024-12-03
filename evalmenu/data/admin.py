from django.contrib import admin
from data.models.ingredient import Ingredient
from data.models.recette import Recette, RecetteIngredient


class RecetteAdmin(admin.ModelAdmin):
    list_display = ["name", "cs", "nutriscore"]


class RecetteIngredientAdmin(admin.ModelAdmin):
    autocomplete_fields = ["ingredient"]


class IngredientAdmin(admin.ModelAdmin):
    search_fields = ["name"]


admin.site.register(Recette, RecetteAdmin)
admin.site.register(RecetteIngredient, RecetteIngredientAdmin)
admin.site.register(Ingredient, IngredientAdmin)
