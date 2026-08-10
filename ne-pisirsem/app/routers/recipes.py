"""
Tariflerle ilgili endpoint'ler: listeleme, detay ve
malzemeye göre tarif önerisi.
"""

from fastapi import APIRouter
from app.schemas.recipe_schemas import IngredientInput, RecipeOut
from app.services.matching_service import find_matching_recipes

router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
)


@router.post("/suggest", response_model=list[RecipeOut])
def suggest_recipes(payload: IngredientInput):
    """
    Kullanıcının elindeki malzemelere göre tarif önerir.

    Örnek istek gövdesi:
    {
        "ingredient_names": ["domates", "soğan", "yumurta"]
    }
    """
    results = find_matching_recipes(payload.ingredient_names, allow_missing=True)
    return results


@router.get("/{recipe_id}")
def get_recipe_detail(recipe_id: int):
    """Bir tarifin detayını getirir: adımlar, püf noktaları, görsel (henüz TODO)."""
    # TODO: recipe_id'ye göre tek tarif + tips alanını çeken sorgu
    return {"message": f"{recipe_id} numaralı tarifin detayı - henüz veritabanına bağlanmadı"}
