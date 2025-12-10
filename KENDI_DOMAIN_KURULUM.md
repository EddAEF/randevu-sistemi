# KENDI DOMAIN'LE VERCEL DEPLOYMENT REHBERI

## 🎯 HEDEF
```
Adım 1: Domain adını al (siteniz.com)
Adım 2: Projeyi Vercel'e deploy et
Adım 3: Domain'i Vercel'e bağla
SONUÇ: https://siteniz.com 🎉
```

---

## 📋 ÖZET - TOPLAM MALİYET

| Masraf | Ücret | Zorunlu? |
|--------|-------|----------|
| Domain (.com) | ~₺30-50/yıl | ✅ Evet |
| Vercel Hosting | **₺0** (ÜCRETSİZ) | ✅ Evet |
| SSL Sertifikası | **₺0** (Otomatik) | ✅ Evet |
| **TOPLAM/YIL** | **~₺30-50** | |

**Yani yılda sadece domain parası ödüyorsunuz!** 💰

---

## 🚀 ADIM 1: DOMAIN ALIMI

### Seçenek A: Türkiye'de Domain Satıcıları

#### ✅ ÖNERILEN: Namecheap
```
1. https://www.namecheap.com aç
2. Domain bul: "siteniz" ara
3. Fiyat kontrol: ~$10.98/yıl (₺350)
4. Sepete ekle
5. Email doğrula
6. Ödeme yap (Kredi kartı)
7. Domain senin! ✅
```

**Avantajlar:**
- Çok ucuz ($10.98)
- Türkiye ödemi alıyor
- Kolay kontrol paneli
- 24/7 destek

#### 📌 ALTERNATIF: TR Domain Satıcıları
- **Netim.com** (₺45/yıl)
- **Nic.tr** (Resmi)
- **Turhost.com** (₺40/yıl)

#### 📌 ALTERNATIF: GoDaddy / Hostinger
- **GoDaddy**: $12.99/yıl (ama pahalı)
- **Hostinger**: $2.99/yıl (ilk yıl)

### ⚠️ ÖNEMLİ: Domain Seçimi İçin İpuçları

```
✅ İyi domain seçimi:
- siteniz.com
- randevusistemi.com
- hizmetlerim.com
- adınyazılımı.com

❌ Kaçınılacaklar:
- randevusistemim123456.com (çok uzun)
- aaaa.com (çok kısa, yanıltıcı)
- sistemirandevu.com (ters)
```

**Domain Seçimi Tamamlandığında:**
```
✅ Domain: siteniz.com
✅ Fiyat: ~$10-15/yıl
✅ Kontrol Panel: Hazır
✅ DNS Ayarları: Hazırlanmış
```

---

## 💻 ADIM 2: PROJEYI VERCEL'E DEPLOY ET

### AŞAMA 1: GitHub'a Yükle (Yapıldı mı kontrol et)

```powershell
# PowerShell'de
cd "C:\Users\HİKMET\Desktop\RANDEVU SİSTEMİ"

# 1. Git kurulu mu?
git --version

# 2. Git config
git config --global user.name "Adın Soyadın"
git config --global user.email "email@gmail.com"

# 3. Projeyi initialize et
git init
git add .
git commit -m "Randevu sistemi başlangıç"
git branch -M main

# 4. GitHub'da https://github.com/new git
# Repo adı: randevu-sistemi
# Public seç
# Create

# 5. Local repo'yu GitHub'a bağla
git remote add origin https://github.com/SENIN_USERNAME/randevu-sistemi.git
git push -u origin main

# ℹ️ Username nedir?
# GitHub hesabınızın @github.com/USERNAME yazan kısım
```

### AŞAMA 2: Vercel'e Deploy Et

```
1. https://vercel.com aç
2. "Sign up" tıkla
3. "GitHub" ile bağlan
4. "Authorize vercel-actions"
5. GitHub hesabını doğrula
6. "Import Project" tıkla
7. "randevu-sistemi" reposunu seç
8. "Import" tıkla
9. Deploy ayarları:
   - Framework: Other (Flask)
   - Build: (boş bırak)
   - Output: (boş bırak)
10. "Deploy" tıkla
11. ⏳ 2-3 dakika bekle
```

### ✅ Sonuç
```
URL: https://randevu-sistemi-xxxxx.vercel.app
✅ Çalışıyor!
✅ HTTPS aktif!
✅ Test et!
```

---

## 🌐 ADIM 3: DOMAIN'İ VERCEL'E BAĞLA

### AŞAMA 1: Namecheap'te DNS Ayarla

```
1. Namecheap.com'da oturum aç
2. "Domain List" tıkla
3. "siteniz.com" bularak "Manage" tıkla
4. "Nameservers" sekmesine git
5. "Vercel Nameservers" i seç VEYA
   
   Vercel NS'ler:
   - ns1.vercel-dns.com
   - ns2.vercel-dns.com
   - ns3.vercel-dns.com

6. SAVE tıkla
```

### AŞAMA 2: Vercel'de Domain Ekle

```
1. Vercel Dashboard'a git
2. Projenize girin (randevu-sistemi)
3. "Settings" tıkla
4. "Domains" sekmesine git
5. "Add Domain" tıkla
6. "siteniz.com" yazı
7. "Add" tıkla
8. DNS verification bekle (⏳ 15-30 dakika)
```

### ✅ Doğrulama Tamamlandıktan Sonra

```
https://siteniz.com
✅ Çalışıyor!
✅ HTTPS aktif!
✅ Tüm insanlar görebilir!
```

---

## 📝 DETAYLI KURULUM TALIMATINI

### 1️⃣ ADIM: GITHUB SETUP

```powershell
# Terminal aç (Windows PowerShell)
cd "C:\Users\HİKMET\Desktop\RANDEVU SİSTEMİ"

# Git var mı kontrol
git --version

# Eğer yok: https://git-scm.com/download/win indirip yükle

# Git kullanıcı bilgisi (gitHub username'ine uygun yap)
git config --global user.name "Adın Soyadı"
git config --global user.email "seninemail@gmail.com"

# Proje klasöründe
git init
git add .
git commit -m "Randevu sistemi - başlangıç"
git branch -M main

# GitHub'da repo oluştur: https://github.com/new
# Repo adı: randevu-sistemi
# Description: Profesyonel Randevu Yönetim Sistemi
# Public: ✓
# Create

# Remote ekle (KULLANICI_ADI'nı değiştir)
git remote add origin https://github.com/KULLANICI_ADI/randevu-sistemi.git

# Push et
git push -u origin main

# ✅ İşlem bitti!
```

**GitHub Push Sırasında Hata?**
```
Problem: "fatal: could not read Password for..."

Çözüm:
1. https://github.com/settings/tokens/new git
2. "Generate new token"
3. Token'ı kopyala
4. PowerShell'de sorulan password'a yapıştır
5. Enter
6. ✅ Çalışır!
```

---

### 2️⃣ ADIM: NAMECHEAP DOMAIN ALIMI

```
AŞAMA 1: Domain Seç
1. https://www.namecheap.com aç
2. Arama kutusuna "siteniz.com" yaz
3. Özel adınız varsa onu kullan
4. Domain'i bul
5. Fiyata bak (~$10-15)

AŞAMA 2: Ödeme
1. "Add to Cart" tıkla
2. "View Cart" tıkla
3. "Proceed to Checkout" tıkla
4. Email kontrol et
5. Ödeme yap (Kredi kartı)
6. Doğrulama emaili bak (spam klasöründe olabilir)

AŞAMA 3: DNS Ayarla
1. Dashboard → Domain List
2. "siteniz.com" → Manage
3. "Nameservers" sekmesi
4. "Vercel Nameservers" i seç

⏳ 15-30 dakika bekleme süresi (DNS yayılması)
```

---

### 3️⃣ ADIM: VERCEL DEPLOYMENT

```
AŞAMA 1: Vercel'e Kaydol
1. https://vercel.com aç
2. "Sign up" tıkla
3. "Continue with GitHub" tıkla
4. GitHub yetkilendirmesi ver
5. Email doğrula

AŞAMA 2: Projeyi İçeri Al
1. https://vercel.com/new aç
2. "Import Project" tıkla
3. GitHub URL'ni gir veya repo seç:
   https://github.com/KULLANICI_ADI/randevu-sistemi
4. "Continue" tıkla

AŞAMA 3: Ayarlar
1. Framework: "Other"
2. Build Command: (boş)
3. Output Directory: (boş)
4. Environment Variables:
   - FLASK_ENV = production
   - FLASK_DEBUG = False
5. "Deploy" tıkla

⏳ 2-3 dakika deploy edilir
```

---

### 4️⃣ ADIM: DOMAIN BAĞLAMA

```
AŞAMA 1: Vercel Settings
1. Vercel Dashboard
2. Projeyi seç (randevu-sistemi)
3. "Settings" tıkla
4. "Domains" sekmesi
5. "Add" tıkla
6. "siteniz.com" yazı
7. "Add Domain" tıkla

AŞAMA 2: DNS Doğrulama
1. Vercel otomatik kontrol eder
2. NS kayıtlarını Namecheap'te ayarladıysanız:
   ✅ Doğru yolda
3. 15-30 dakika bekleme
4. ✅ Domain bağlı!

AŞAMA 3: Test Et
1. https://siteniz.com aç
2. Randevu sistemi açılsın
3. Admin: https://siteniz.com/admin
4. Hepsi çalışmalı
```

---

## 🔍 NAMECHEAP'TE DOMAIN YÖNETIMI

### DNS Ayarlarını Kontrol Etme

```
Namecheap Dashboard:
1. Domain List
2. "siteniz.com" → Manage
3. "Nameservers" sekmesi
4. Şu nameservers görülmeli:
   
   ✅ ns1.vercel-dns.com
   ✅ ns2.vercel-dns.com
   ✅ ns3.vercel-dns.com

5. Eğer Custom DNS seçiliyse:
   - "Vercel Nameservers" seç
   - Save

6. Domain sekmesi:
   - Status: Active ✓
   - Renewal: Auto-renew (opsiyonel)
```

### Subdomain Eklemek (İsteğe Bağlı)

```
Örnekler:
- admin.siteniz.com (ayrı sayfa)
- blog.siteniz.com (blog)
- api.siteniz.com (API)

Namecheap'te:
1. Advanced DNS sekmesi
2. Add Record
   - Type: A
   - Name: admin (veya blog)
   - Value: [Vercel IP]
3. Save

VEYA daha kolay:
- Vercel'de subdomain ekle
- Otomatik DNS yapılandırması olur
```

---

## ⚙️ VERCEL AYARLARINI DÜZENLE

### Environment Variables (Önemli!)

```
Vercel Dashboard → Settings → Environment Variables

FLASK_ENV = production
FLASK_DEBUG = False
DATABASE_URL = (opsiyonel)
SECRET_KEY = (Flask gizli anahtar)
```

### Build & Deploy

```
Settings → Build & Development Settings:
- Build Command: pip install -r requirements.txt
- Output Directory: (boş)
- Install Command: (boş)
- Development Command: (boş)

SAVE tıkla
```

### Custom Domain

```
Settings → Domains:
1. Add Domain
2. siteniz.com
3. Doğrulama
4. ✅ Bağlı!
```

---

## 🧪 TEST KONTROL LİSTESİ

### Deploy Sonrası Test Et

```
□ https://siteniz.com açılıyor
□ Tüm sayfalar görünüyor
□ CSS/resimler yükleniyor
□ Form çalışıyor
□ Admin paneli açılıyor
□ Hiçbir hata mesajı yok
□ Sayfa hızlı yükleniyor
□ Mobil'de görünüyor
```

### Vercel Dashboard Kontrol

```
Vercel Dashboard:
□ Build Status: ✅ Success
□ Deployment: ✅ Production
□ Domain: ✅ siteniz.com
□ SSL: ✅ Active (https)
□ Logs: Hatasız
```

---

## 🚨 SORUN GİDERİCİ

### Problem: Domain bağlanmamış, "Not Found" hatası

**Çözüm:**
```
1. Namecheap'te Nameservers kontrol et:
   ✓ ns1.vercel-dns.com
   ✓ ns2.vercel-dns.com
   ✓ ns3.vercel-dns.com

2. 30 dakika bekleme (DNS yayılması)

3. Test: https://dns.google.com
   - siteniz.com ara
   - Vercel NS'ler gözükmeli

4. Yine yapmazsa:
   - Namecheap Cache temizle
   - Vercel → Redeploy
```

### Problem: https://siteniz.com açılmadı ama vercel.app açıldı

**Çözüm:**
```
1. Vercel Dashboard → Domains kontrol
2. siteniz.com ekli mi?
3. Status: "Verified" mi?
4. Value/CNAME doğru mu?
5. 30 dakika daha bekleme
6. Browser cache temizle (Ctrl+Shift+Delete)
```

### Problem: Vercel'de SSL hatası

**Çözüm:**
```
Vercel otomatik SSL verir, ama:

1. Domain bağlı olmalı
2. DNS yayılmış olmalı (24-48 saat)
3. Vercel ayarlar → Domains → siteniz.com
4. Certificate status kontrol
5. 48 saat bekleme
```

### Problem: Eski siteniz varsa conflict

**Çözüm:**
```
Domain transfer gerekirse:
1. Eski hosting'den domain'i unlokla
2. Auth code al
3. Namecheap'te transfer başlat
4. 5-7 gün bekle
5. Sonra Vercel'e bağla

VEYA:
Eski hostu koru, Vercel subdomain kullan:
- randevu.siteniz.com (Vercel)
- siteniz.com (Eski)
```

---

## 📊 ZAMAN ÇIZELGESI

```
┌─────────────────────────────────────────────────────┐
│ Adım                    │ Zaman    │ Bekleme        │
├─────────────────────────────────────────────────────┤
│ 1. GitHub Push          │ 2 dakika │ -              │
│ 2. Domain Satın Al      │ 5 dakika │ 15 dk          │
│ 3. Nameservers Ayarla   │ 1 dakika │ 15-30 dk       │
│ 4. Vercel Deploy        │ 2 dakika │ 2-3 dk         │
│ 5. Domain Bağla         │ 1 dakika │ Otomatik       │
│ 6. DNS Yayılması        │ -        │ 15-30 dk       │
│ 7. Test                 │ 2 dakika │ -              │
├─────────────────────────────────────────────────────┤
│ TOPLAM AKTIF ZAMAN      │ ~15 dk   │                │
│ TOPLAM BEKLEME          │ -        │ ~1 saat        │
│ **GENEL TOPLAM**        │ **~1-2 saat** │         │
└─────────────────────────────────────────────────────┘
```

---

## ✅ FINAL CHECKLIST

### Başlamadan Önce:
```
□ GitHub hesabı var mı?
□ Kredi kartı var mı? (Namecheap ödeme için)
□ Proje dosyaları hazır mı?
□ requirements.txt dosyası var mı?
```

### GitHub Aşaması:
```
□ Git yüklü
□ Proje GitHub'a push edildi
□ Repo: github.com/KULLANICI/randevu-sistemi
□ Public repo olarak ayarlandı
```

### Domain Aşaması:
```
□ Domain adı kararlaştırıldı
□ Namecheap'te domain satın alındı
□ Nameservers Vercel'e ayarlandı
```

### Vercel Aşaması:
```
□ Vercel hesabı oluşturuldu
□ GitHub bağlandı
□ Proje import edildi
□ Deploy başarılı (✅ Success)
□ Vercel.app URL çalışıyor
```

### Domain Bağlama Aşaması:
```
□ Vercel'de domain eklendi
□ DNS doğrulaması yapıldı
□ siteniz.com açılıyor
□ HTTPS aktif (🔒)
```

### Nihai Kontrol:
```
□ https://siteniz.com ana sayfa açılıyor
□ https://siteniz.com/admin admin paneli açılıyor
□ Form çalışıyor
□ Veri kaydediliyor
□ Hocaya gösterebilir hale geldi! 🎉
```

---

## 💡 PRO İPUÇLARI

### 1. GitHub'dan Vercel'e Otomatik Güncelleme

```
Ne yaparsanız yapın:
git push origin main

Vercel OTOMATIK olarak:
1. Yeni kodu indiriyor
2. Build yapıyor
3. Deploy ediyor
4. Test ediyor

✅ Kendi website'niz güncellenir!
```

### 2. Domain Yenileme

```
Namecheap'te:
- Auto-renew açık bırak
- Her yıl otomatik yenileme
- Karttan para çekilir
- Huzursuz kalmazsınız
```

### 3. Email Kurulumu (İsteğe Bağlı)

```
Namecheap EmailHosting:
- sizenin@siteniz.com email açabilirsiniz
- Ücretli (opsiyonel)
- Şimdilik gerekmez
```

### 4. Analytics Eklemek

```
Vercel Dashboard:
- Built-in analytics var
- Ziyaretçi sayısı
- Load time
- Error rates
- Otomatik tracking
```

### 5. Environment Secrets

```
Vercel Settings → Environment Variables:
- Gizli veriler buraya koy
- API keys
- Passwords
- Production secrets
```

---

## 📞 HIZA ERIŞIM LİNKLERİ

```
GitHub: https://github.com
Namecheap: https://www.namecheap.com
Vercel: https://vercel.com
Vercel Docs: https://vercel.com/docs

GitHub Setup: https://docs.github.com/en/get-started
Flask Deploy: https://flask.palletsprojects.com/en/3.0.x/
```

---

## 🎉 BAŞARILI OLDUĞUNUZDA

```
✅ https://siteniz.com
✅ HTTPS SSL aktif (🔒)
✅ 7/24 online
✅ Herkesin açabileceği
✅ Hocaya gösterebileceğiniz
✅ Profesyonel görünümlü

TAMAMLANDI! 🚀
```

---

## 📝 HIZLI REFERANS

### Adım 1: GitHub
```powershell
cd "C:\Users\HİKMET\Desktop\RANDEVU SİSTEMİ"
git init
git add .
git commit -m "başlangıç"
git branch -M main
git remote add origin https://github.com/USERNAME/randevu-sistemi.git
git push -u origin main
```

### Adım 2: Namecheap
```
1. Domain satın al
2. Nameservers:
   - ns1.vercel-dns.com
   - ns2.vercel-dns.com
   - ns3.vercel-dns.com
```

### Adım 3: Vercel
```
1. vercel.com/new
2. GitHub repo seç
3. Deploy
4. Settings → Domains → siteniz.com
5. DONE!
```

---

**Soruların varsa, sorma çekinme!** 🤝
