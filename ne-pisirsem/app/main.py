"""
Ne Pişirsem - Ana uygulama giriş noktası

Bu dosya FastAPI uygulamasını başlatır ve router'ları (URL yollarını) birbirine bağlar.
Çalıştırmak için: uvicorn app.main:app --reload
"""

from fastapi import FastAPI
from app.routers import ingredients, recipes

app = FastAPI(
    title="Ne Pişirsem API",
    description="Elindeki malzemelerle yapabileceğin yemekleri öneren, "
                 "Türk ve dünya mutfağından tarifler sunan uygulama",
    version="0.1.0",
)

# Router'ları uygulamaya ekliyoruz.
# Her router, belirli bir konuyla ilgili endpoint'leri (URL'leri) gruplar.
app.include_router(ingredients.router)
app.include_router(recipes.router)


@app.get("/")
def read_root():
    """API çalışıyor mu diye kontrol etmek için basit bir sağlık kontrolü."""
    return {"message": "Ne Pişirsem API çalışıyor 🍳"}
