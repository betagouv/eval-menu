from django.contrib import admin
from data.models.ingredient import Ingredient
from data.models.recette import Recette, RecetteIngredient


class RecetteAdmin(admin.ModelAdmin):
    pass

class RecetteIngredientAdmin(admin.ModelAdmin):
    pass

class IngredientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recette, RecetteAdmin)
admin.site.register(RecetteIngredient, RecetteIngredientAdmin)
admin.site.register(Ingredient, IngredientAdmin)