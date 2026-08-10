# Ne Pişirsem 🍳

Elindeki malzemelerle ne pişirebileceğini söyleyen, Türk ve dünya mutfağından
tarifler sunan bir uygulama.

## Fikrin çıkış noktası

Ailemdeki kadınların (annem, babaannem, halalarım) neredeyse her gün
"bugün ne pişirsem" diye düşünmesinden yola çıktım. Amaç: kullanıcı elindeki
malzemeleri yazsın (ileride fotoğrafla da eklenecek), uygulama ona hem tam
hem de birkaç malzemesi eksik olsa da yapabileceği tarifleri önersin.

## Planlanan özellikler

- [x] Proje iskeleti (FastAPI + SQL Server)
- [ ] Malzeme girişi (yazarak) + tarif önerisi (tam / eksik eşleşme)
- [ ] Türk ve dünya mutfağı kategorileri (yemek / tatlı ayrımı)
- [ ] Her tarifte: görsel, adımlar, **püf noktaları**, yorumlar
- [ ] Kullanıcıların kendi tarif varyasyonlarını eklemesi
- [ ] Mobil arayüz (Flutter)
- [ ] Fotoğraftan malzeme tanıma (Azure Computer Vision)
- [ ] Azure'a deploy

## Teknoloji

- **Backend:** Python, FastAPI
- **Veritabanı:** SQL Server
- **Arayüz (planlanan):** Flutter
- **Bulut (planlanan):** Azure

## Proje yapısı

```
app/
├── main.py              # FastAPI giriş noktası
├── database/             # Veritabanı bağlantısı
├── models/                # Veritabanı tablo tanımları (yakında)
├── schemas/               # API veri şemaları (Pydantic)
├── routers/                # API endpoint'leri
└── services/                # İş mantığı (malzeme eşleştirme vb.)
```

## Kurulum (yerel geliştirme)

```bash
# Bağımlılıkları yükle
pip install -r requirements.txt

# .env dosyasını oluştur
cp .env.example .env
# .env içindeki bilgileri kendi SQL Server ayarlarınla doldur

# Sunucuyu başlat
uvicorn app.main:app --reload
```

Sunucu ayağa kalkınca `http://127.0.0.1:8000/docs` adresinden API'yi
tarayıcıdan test edebilirsin (Swagger arayüzü).

## Durum

Şu an aktif geliştirme aşamasında — backend ve veritabanı şeması üzerinde
çalışılıyor.
