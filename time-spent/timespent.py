from datetime import datetime, timedelta

# Doğum tarihinizi ve saati girin
dogum_tarihi = datetime(1996, 7, 3, 22, 50)  # Örneğin: Benim doğum tarihim Yıl, Ay, Gün, Saat = 1996-7-3 22:50

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
