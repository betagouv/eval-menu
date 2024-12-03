import json
import uuid

from data.models.ingredient import Ingredient
from data.models.recette import Recette, RecetteIngredient


def show_ingredients(export_path: str):
    '''Test fuction not used anymore in 'exportecobalyse' django command'''
    print("Read ingredients from database")
    ingredients = Ingredient.objects.all()
    ingr_list = list(ingredients.values())
    print(ingr_list)


def export_recipes(export_path: str):
    print(f'Read recipes from database and export them to json file: {export_path}')
    
    recipes = Recette.objects.all()    
    export_data = []
    for recipe in recipes:        
        # ecobalyse recipe format
        export_recipe = {
            'id': str(uuid.uuid4()), 
            'name': recipe.name, 
            'scope': 'food', 
            'category': '', 
            'query': {
                'ingredients': [], 
            }
        }
        #print(f"Recipe: ({recipe['id']}) {recipe['name']}")

        # populate ingredients list of 'export_recipe'
        res = RecetteIngredient.objects.filter(recette_id=recipe.id).select_related('ingredient')
        for recipe_ingr in res:
            ingr_name = recipe_ingr.ingredient.id_ecobalyse
            ingr_mass = int(recipe_ingr.poids)
            
            export_ingr = {
                'id': ingr_name, 
                'mass': ingr_mass
            }
            #print(export_ingr)
            export_recipe['query']['ingredients'].append(export_ingr)
        export_data.append(export_recipe)    
    
    print(export_data)
    with open(export_path, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, indent=2, ensure_ascii=False)
    