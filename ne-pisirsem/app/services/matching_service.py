"""
Malzeme eşleştirme mantığı.

Burası uygulamanın "beyni": kullanıcının elindeki malzemelerle
veritabanındaki tarifleri karşılaştırıp en uygun olanları sıralar.

Bu dosyada SQL sorgusu, connection.py'deki get_connection() ile açılan
bağlantı üzerinden çalışır. Şema henüz veritabanına işlenmediği için
aşağıdaki sorgu, birlikte tasarladığımız tabloları (recipes,
ingredients, recipe_ingredients) varsayıyor.
"""

from app.database.connection import get_connection


def find_matching_recipes(user_ingredients: list[str], allow_missing: bool = True):
    """
    Kullanıcının verdiği malzeme listesine göre tarifleri sıralar.

    Mantık:
    1. Her tarif için, tarifin ZORUNLU (is_optional = 0) malzemelerinden
       kaçının kullanıcıda olduğunu say.
    2. Zorunlu malzemesi tam eşleşenler en üstte.
    3. allow_missing=True ise, 1-2 zorunlu malzemesi eksik olan tarifler
       de "eksik malzemeyle en yakın eşleşenler" olarak listeye girer.
    4. Opsiyonel (is_optional = 1) malzemeler eksik olsa da tarifi elemez.

    NOT: Bu fonksiyon henüz test edilmedi, veritabanı kurulunca
    birlikte çalıştırıp doğrulayacağız.
    """
    if not user_ingredients:
        return []

    placeholders = ",".join("?" for _ in user_ingredients)

    query = f"""
        SELECT
            r.recipe_id,
            r.name,
            r.cuisine_type,
            r.category,
            COUNT(CASE WHEN ri.is_optional = 0 AND i.name IN ({placeholders})
                       THEN 1 END) AS matched_required,
            COUNT(CASE WHEN ri.is_optional = 0 THEN 1 END) AS total_required
        FROM recipes r
        JOIN recipe_ingredients ri ON r.recipe_id = ri.recipe_id
        JOIN ingredients i ON ri.ingredient_id = i.ingredient_id
        GROUP BY r.recipe_id, r.name, r.cuisine_type, r.category
        ORDER BY matched_required DESC
    """

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, user_ingredients)
    rows = cursor.fetchall()
    conn.close()

    results = []
    for row in rows:
        matched = row.matched_required
        total = row.total_required
        missing_count = total - matched

        # Tam eşleşenleri her zaman göster.
        # Eksik olanları, sadece allow_missing açıksa ve az sayıda eksik varsa göster.
        if missing_count == 0 or (allow_missing and missing_count <= 2):
            results.append({
                "recipe_id": row.recipe_id,
                "name": row.name,
                "cuisine_type": row.cuisine_type,
                "category": row.category,
                "matched_ingredient_count": matched,
                "total_ingredient_count": total,
            })

    return results
