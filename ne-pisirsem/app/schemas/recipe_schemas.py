"""
Pydantic şemaları.

Bunlar veritabanı tabloları DEĞİL — API'ye giren/çıkan verinin
şeklini ve tipini tanımlıyorlar. FastAPI bunları otomatik doğrulama
(validation) ve dokümantasyon (Swagger) için kullanır.
"""

from pydantic import BaseModel
from typing import List, Optional


class IngredientInput(BaseModel):
    """Kullanıcının elindeki malzemeleri gönderirken kullanacağı format."""
    ingredient_names: List[str]  # örn: ["domates", "soğan", "yumurta"]


class RecipeOut(BaseModel):
    """Bir tarifi API'den dışarı verirken kullanılan format."""
    recipe_id: int
    name: str
    cuisine_type: str
    category: str  # "yemek" ya da "tatlı"
    matched_ingredient_count: int
    total_ingredient_count: int
    missing_ingredients: List[str] = []

    class Config:
        from_attributes = True


class RecipeDetailOut(RecipeOut):
    """Tarif detay sayfası için ekstra alanlar: adımlar ve püf noktaları."""
    instructions: str
    tips: Optional[str] = None
    prep_time_minutes: Optional[int] = None
