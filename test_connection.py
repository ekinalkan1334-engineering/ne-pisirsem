"""
Bu script, FastAPI'yi hiç devreye sokmadan SQL Server bağlantısını
doğrudan test eder. Hata varsa direkt burada, açıkça görünür.
"""

from app.database.connection import get_connection

print("Bağlantı deneniyor...")

try:
    conn = get_connection()
    print("BAŞARILI: Veritabanına bağlandı!")

    cursor = conn.cursor()
    cursor.execute("SELECT name FROM ingredients")
    rows = cursor.fetchall()

    print(f"\n{len(rows)} malzeme bulundu:")
    for row in rows:
        print(f"  - {row.name}")

    conn.close()

except Exception as e:
    print("\nHATA OLUŞTU:")
    print(type(e).__name__)
    print(str(e))
