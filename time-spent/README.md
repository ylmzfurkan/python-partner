# Geçen Süre Hesaplama

Bu Python programı, doğum tarihinizden itibaren dünya üzerinde geçirdiğiniz süreyi hesaplar. Örnekte, geçen süreyi yıl, ay, gün, saat ve dakika cinsinden ekrana bastırır.

## Kullanım

1. `gecen_sure.py` dosyasını açın.
2. `dogum_tarihi` değişkenini kendi doğum tarihiniz ve saatinizle güncelleyin.
3. Kodu çalıştırın.
4. Geçen süre sonucu ekranda görünecektir.

## Örnek

```python
from datetime import datetime, timedelta

# Doğum tarihinizi ve saati girin
dogum_tarihi = datetime(1990, 5, 15, 9, 30)  # Örneğin: 1990-05-15 09:30

# Şu anki zamanı alın
simdiki_zaman = datetime.now()

# Geçen süreyi hesaplayın
gecen_zaman = simdiki_zaman - dogum_tarihi

# Yılları, ayları, günleri, saatleri ve dakikaları hesaplayın
yillar = gecen_zaman.days // 365
aylar = (gecen_zaman.days % 365) // 30
gunler = (gecen_zaman.days % 365) % 30
saatler = gecen_zaman.seconds // 3600
dakikalar = (gecen_zaman.seconds % 3600) // 60

# Sonucu ekrana bastırın
print(f"{yillar} Yıl, {aylar} Ay, {gunler} Gün, {saatler} Saat, {dakikalar} Dakika")
