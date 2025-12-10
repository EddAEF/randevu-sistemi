# Randevu Sistemi Konfigürasyonu

# Flask Ayarları
DEBUG = True
TESTING = False

# Veritabanı
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False

# Session
PERMANENT_SESSION_LIFETIME = 86400  # 24 saat

# Upload
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

# Hizmet Türleri
HIZMETLER = [
    'Danışmanlık',
    'Teknik Destek',
    'Raporlama',
    'Güvenlik',
    'Müşteri Hizmetleri',
    'Proje Yönetimi'
]

# Çalışma Saatleri
SAAT_LISTESI = [
    '09:00', '09:30', '10:00', '10:30',
    '11:00', '11:30', '14:00', '14:30',
    '15:00', '15:30', '16:00', '16:30',
    '17:00'
]

# Email Konfigürasyonu (isteğe bağlı)
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'your-email@gmail.com'
MAIL_PASSWORD = 'your-password'
MAIL_DEFAULT_SENDER = 'noreply@randevusistemi.com'

# İletişim Bilgileri
CONTACT_PHONE = '+90 (555) 123-4567'
CONTACT_EMAIL = 'info@randevusistemi.com'
CONTACT_ADDRESS = 'İstanbul, Türkiye'

# Sosyal Medya
SOCIAL_MEDIA = {
    'facebook': 'https://facebook.com/randevusistemi',
    'twitter': 'https://twitter.com/randevusistemi',
    'instagram': 'https://instagram.com/randevusistemi',
    'linkedin': 'https://linkedin.com/company/randevusistemi'
}
