# 🎯 Profesyonel Randevu Sistemi

Modern, responsive ve production-ready bir randevu yönetim sistemi.

## ✨ Özellikler

- **Responsive Tasarım**: Mobil, tablet ve masaüstü uyumlu
- **Modern Arayüz**: Gradient, animasyonlar ve smooth transitions
- **Veritabanı Desteği**: SQLite ile veri saklama
- **API Endpoints**: Admin panel ve entegrasyonlar için
- **Validasyon**: Client-side ve server-side doğrulama
- **İstatistikler**: Randevu durumlarını takip etme
- **Güvenlik**: Şifreli veriler ve hata yönetimi

## 📋 Gereksinimleri

- Python 3.8+
- Flask 3.0+
- Flask-SQLAlchemy 3.1+

## 🚀 Kurulum ve Çalıştırma

### 1. Gereksinimleri Yükle

```bash
pip install -r requirements.txt
```

### 2. Uygulamayı Çalıştır (Geliştirme)

```bash
python app.py
```

Uygulama `http://localhost:5000` adresinde çalışacaktır.

### 3. Production İçin Dağıtım

Üretim ortamında `python app.py` yerine aşağıdakini kullanın:

#### Gunicorn ile:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

#### Nginx Reverse Proxy Konfigürasyonu:
```nginx
server {
    listen 80;
    server_name randevusistemi.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static/ {
        alias /path/to/app/static/;
    }
}
```

#### Systemd Service (Linux):
```ini
[Unit]
Description=Randevu Sistemi
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/randevu-sistemi
ExecStart=/usr/bin/gunicorn -w 4 -b 127.0.0.1:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

## 📁 Dosya Yapısı

```
randevu-sistemi/
├── app.py                 # Ana Flask uygulaması
├── requirements.txt       # Python bağımlılıkları
├── randevular.db         # SQLite veritabanı (otomatik oluşturulur)
├── static/
│   └── style.css         # Responsive CSS stilleri
└── templates/
    └── index.html        # HTML şablonu
```

## 🔌 API Endpoints

### Randevu Oluştur
- **POST** `/randevu-al`
- Form verisi ile randevu oluştur

### Tüm Randevuları Al
- **GET** `/api/randevular`
- JSON formatında tüm randevuları getir

### Belirli Randevuyu Al
- **GET** `/api/randevular/<id>`
- Tek bir randevunun detaylarını getir

### Randevu Durumunu Güncelle
- **POST** `/api/randevular/<id>/durum`
- JSON: `{"durum": "Onaylandı"}`

### Randevu Sil
- **DELETE** `/api/randevular/<id>`
- Belirli bir randevuyu sil

### İstatistikler
- **GET** `/api/istatistikler`
- Randevu istatistiklerini getir

## 🎨 Özelleştirme

### Hizmet Türlerini Değiştir
`templates/index.html` dosyasında hizmet seçeneklerini düzenle:

```html
<option value="Danışmanlık">Danışmanlık</option>
<option value="Teknik Destek">Teknik Destek</option>
<!-- Kendi hizmetlerinizi ekle -->
```

### Renkleri Değiştir
`static/style.css` dosyasında color variables'ı düzenle:

```css
:root {
    --primary: #1a3a52;      /* Ana renk */
    --secondary: #f39c12;    /* İkincil renk */
    /* Diğer renkler... */
}
```

### İletişim Bilgilerini Güncelle
`templates/index.html` dosyasında footer bölümünü düzenle

## 🔒 Güvenlik İpuçları

1. **Secret Key Değiştir**: `app.py` dosyasında `app.secret_key` değerini değiştir
2. **HTTPS Kullan**: Production'da her zaman HTTPS kullan
3. **CORS Konfigürasyonu**: Gerekirse CORS policy'sini ayarla
4. **Rate Limiting**: DDoS saldırılarına karşı rate limiting ekle
5. **Input Validation**: Tüm girişleri server-side'da valide et

## 📊 Veritabanı Yedekleme

```bash
# Veritabanını yedekle
cp randevular.db randevular.db.backup

# Eski veritabanını restore et
cp randevular.db.backup randevular.db
```

## 🛠️ Sorun Giderme

### Veritabanı Hatası
```bash
# Veritabanını sıfırla
rm randevular.db
python app.py
```

### Port 5000 Kullanımda
```bash
# Farklı port kullan
python -c "from app import app; app.run(port=8000)"
```

## 📞 İletişim Desteği

Sorunlar veya öneriler için iletişime geçin.

## 📝 Lisans

Bu proje MIT Lisansı altında yayımlanmıştır.

---

**Not**: Production ortamında güvenlik ayarlarını gözden geçirmeyi unutmayın!
