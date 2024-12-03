# utils.py
import requests


def get_nutriscore(ingredients_text):
    print(f"Calling openfoodfacts API with text {ingredients_text}")
    payload = {
        "fields": "ingredients,nutriments_estimated,nutriscore_grade,nutriscore_score,ecoscore_grade,ecoscore_score",
        "lc": "fr",
        "product": {
            "lang": "fr",
            "categories_tags": ["Cassoulets au confit de canard"],
            "ingredients_text_fr": ingredients_text,
            "tags_lc": "fr",
        },
    }

    headers = {"Content-Type": "application/json"}

    url = "https://world.openfoodfacts.dev/api/v3/product/test"  # URL de votre API
    response = requests.patch(url, json=payload, headers=headers).json()
    if "product" in response.keys():
        if "nutriscore_grade" in response["product"].keys():
            return response["product"]["nutriscore_grade"]
