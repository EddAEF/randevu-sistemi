# 🚀 Hosting ve Yayınlama Rehberi

Randevu Sisteminizi web'de canlı hale getirmek için adım adım rehber.

## 📦 Seçenek 1: Heroku'da Yayınlama (En Kolay)

### 1. Hazırlanma
```bash
pip install gunicorn
```

### 2. Procfile Oluştur
Proje kökünde `Procfile` dosyası oluştur:
```
web: gunicorn app:app
```

### 3. requirements.txt Güncelleştir
```bash
pip freeze > requirements.txt
```

### 4. Git Repository Oluştur
```bash
git init
git add .
git commit -m "Initial commit"
```

### 5. Heroku'ya Deploy Et
```bash
heroku login
heroku create randevu-sistemi
git push heroku main
```

URL: `https://randevu-sistemi.herokuapp.com`

---

## 🖥️ Seçenek 2: Linux VPS'de Yayınlama (Recommended)

### 1. VPS'e Bağlan
```bash
ssh root@your_server_ip
```

### 2. Sistem Paketleri Yükle
```bash
apt update
apt install python3-pip python3-venv nginx
```

### 3. Proje Dizini Oluştur
```bash
mkdir /var/www/randevu-sistemi
cd /var/www/randevu-sistemi
```

### 4. Virtual Environment Oluştur
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
```

### 5. Systemd Service Oluştur
`/etc/systemd/system/randevu.service` dosyasını oluştur:
```ini
[Unit]
Description=Randevu Sistemi Flask App
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/randevu-sistemi
Environment="PATH=/var/www/randevu-sistemi/venv/bin"
ExecStart=/var/www/randevu-sistemi/venv/bin/gunicorn -w 4 -b 127.0.0.1:5000 app:app
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Service'i aktifleştir:
```bash
systemctl daemon-reload
systemctl start randevu
systemctl enable randevu
```

### 6. Nginx Yapılandır
`/etc/nginx/sites-available/randevu` oluştur:
```nginx
server {
    listen 80;
    server_name randevusistemi.com www.randevusistemi.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
    }

    location /static/ {
        alias /var/www/randevu-sistemi/static/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
```

Site'i etkinleştir:
```bash
ln -s /etc/nginx/sites-available/randevu /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx
```

### 7. SSL Sertifikası (Let's Encrypt)
```bash
apt install certbot python3-certbot-nginx
certbot --nginx -d randevusistemi.com -d www.randevusistemi.com
```

---

## ☁️ Seçenek 3: PythonAnywhere'de Yayınlama

### 1. Hesap Oluştur
[pythonanywhre.com](https://www.pythonanywhere.com) adresinde hesap oluştur

### 2. Web App Oluştur
- New web app
- Flask seç
- Python 3.9+ seç

### 3. Dosyaları Yükle
- Upload files seçeneği ile dosyaları yükle
- WSGI file'ını düzenle

### 4. Veritabanı Ayarını Güncelle
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/username/mysite/randevular.db'
```

---

## 🔐 Güvenlik Checklist

### Production Deployment Öncesi

- [ ] `app.secret_key` değiştir
```python
app.secret_key = 'karmasik-ve-guvenli-bir-anahtar-degistir-bunu'
```

- [ ] Debug modu kapat
```python
app.run(debug=False)
```

- [ ] HTTPS/SSL kullan (Let's Encrypt)

- [ ] CORS politikasını ayarla
```python
from flask_cors import CORS
CORS(app)
```

- [ ] Rate limiting ekle
```python
from flask_limiter import Limiter
limiter = Limiter(app)

@app.route('/randevu-al', methods=['POST'])
@limiter.limit("5/hour")
def randevu_al():
    ...
```

- [ ] Veritabanını yedekle
- [ ] Logging ayarla
- [ ] Error monitoring (Sentry, etc.)

---

## 📊 Veritabanı Yönetimi

### Yedekleme
```bash
# Günlük otomatik backup (Cron job)
0 2 * * * cp /var/www/randevu-sistemi/randevular.db /backup/randevular.db.$(date +\%Y\%m\%d)
```

### Restore
```bash
cp /backup/randevular.db.20250110 /var/www/randevu-sistemi/randevular.db
systemctl restart randevu
```

---

## 📈 Monitoring ve Logging

### Gunicorn Log
```bash
journalctl -u randevu -f
```

### Nginx Log
```bash
tail -f /var/log/nginx/error.log
tail -f /var/log/nginx/access.log
```

### Python Logging
```python
import logging

logging.basicConfig(
    filename='randevu.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

---

## 🚨 Sorun Giderme

### 500 Internal Server Error
```bash
systemctl restart randevu
journalctl -u randevu -n 50
```

### Port Zaten Kullanımda
```bash
# Portu bul
lsof -i :5000

# Kill et
kill -9 [PID]
```

### Veritabanı Hatası
```bash
# Veritabanını sıfırla
rm /var/www/randevu-sistemi/randevular.db
systemctl restart randevu
```

---

## 📞 Destek

Sorunlar için lütfen:
1. Log dosyalarını kontrol et
2. Veritabanı bağlantısını test et
3. Flask debug modunu aç ve hataları kontrol et

---

**Not**: Production ortamında her zaman güvenlik en birinci önceliktir!
