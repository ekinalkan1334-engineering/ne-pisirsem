"""
Bu script, API'nin /recipes/suggest endpoint'inin arka planda çağırdığı
find_matching_recipes fonksiyonunu doğrudan çalıştırır. Hata varsa
tam olarak burada, açıkça görünür.
"""

from app.services.matching_service import find_matching_recipes

print("Tarif önerisi test ediliyor...")

try:
    results = find_matching_recipes(["domates", "soğan", "yumurta"], allow_missing=True)
    print("BAŞARILI!")
    print(results)

except Exception as e:
    print("\nHATA OLUŞTU:")
    print(type(e).__name__)
    print(str(e))
