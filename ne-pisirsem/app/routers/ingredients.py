"""
Malzemelerle ilgili endpoint'ler.

Şimdilik iskelet halinde - veritabanı kurulunca gerçek sorgularla dolduracağız.
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/ingredients",
    tags=["ingredients"],
)


@router.get("/")
def list_ingredients():
    """Veritabanındaki tüm malzemeleri listeler (henüz TODO)."""
    # TODO: SELECT * FROM ingredients sorgusu buraya gelecek
    return {"message": "Malzeme listesi endpoint'i - henüz veritabanına bağlanmadı"}
