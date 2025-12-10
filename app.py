from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime
import os

# Flask Uygulamasını Oluştur
app = Flask(__name__)

# Mail Konfigürasyonu
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

mail = Mail(app)

# Veritabanı Yapılandırması
basedir = os.path.abspath(os.path.dirname(__file__))
default_db_uri = 'sqlite:///' + os.path.join(basedir, 'randevular.db')

# Ortak konfigürasyonları yükle (config.py) ve env ile override et
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', default_db_uri)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = app.config.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)
app.secret_key = os.environ.get(
    'SECRET_KEY',
    app.config.get('SECRET_KEY', 'randevu-sistemi-secret-key-2025')
)

# Veritabanı
db = SQLAlchemy(app)

# Randevu Model
class Randevu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ad_soyad = db.Column(db.String(100), nullable=False)
    telefon = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    tarih = db.Column(db.String(10), nullable=False)
    saat = db.Column(db.String(5), nullable=False)
    hizmet = db.Column(db.String(100), nullable=False)
    konu = db.Column(db.String(200), nullable=False)
    aciklama = db.Column(db.Text, nullable=True)
    durum = db.Column(db.String(20), default='Onay Beklemede')
    olusturma_tarihi = db.Column(db.DateTime, default=datetime.now)
    
    def __repr__(self):
        return f'<Randevu {self.ad_soyad}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'ad_soyad': self.ad_soyad,
            'telefon': self.telefon,
            'email': self.email,
            'tarih': self.tarih,
            'saat': self.saat,
            'hizmet': self.hizmet,
            'konu': self.konu,
            'aciklama': self.aciklama,
            'durum': self.durum,
            'olusturma_tarihi': self.olusturma_tarihi.strftime('%d.%m.%Y %H:%M')
        }

# Veritabanı Oluştur
with app.app_context():
    db.create_all()

# Ana Sayfa
@app.route('/')
def index():
    return render_template('index.html')

# Admin Paneli
@app.route('/admin')
def admin():
    return render_template('admin.html')

# Randevu Oluştur
@app.route('/randevu-al', methods=['POST'])
def randevu_al():
    try:
        ad_soyad = request.form.get('ad_soyad', '').strip()
        telefon = request.form.get('telefon', '').strip()
        email = request.form.get('email', '').strip()
        tarih = request.form.get('tarih', '').strip()
        saat = request.form.get('saat', '').strip()
        hizmet = request.form.get('hizmet', '').strip()
        konu = request.form.get('konu', '').strip()
        aciklama = request.form.get('aciklama', '').strip()
        
        # Validasyon
        if not all([ad_soyad, telefon, email, tarih, saat, hizmet, konu]):
            return render_template('index.html', 
                error_message='Lütfen tüm zorunlu alanları doldurunuz!')
        
        # Email validasyonu
        if '@' not in email or '.' not in email:
            return render_template('index.html', 
                error_message='Lütfen geçerli bir e-posta adresi giriniz!')
        
        # Yeni Randevu Oluştur
        yeni_randevu = Randevu(
            ad_soyad=ad_soyad,
            telefon=telefon,
            email=email,
            tarih=tarih,
            saat=saat,
            hizmet=hizmet,
            konu=konu,
            aciklama=aciklama,
            durum='Onay Beklemede'
        )
        
        db.session.add(yeni_randevu)
        db.session.commit()
        
        # E-posta Gönderimi
        try:
            msg = Message('Randevu Talebiniz Alındı',
                          recipients=[email])
            msg.body = f"""Sayın {ad_soyad},
            
Randevu talebiniz başarıyla alınmıştır. Detaylar aşağıdadır:

Tarih: {tarih}
Saat: {saat}
Hizmet: {hizmet}
Konu: {konu}

En kısa sürede sizinle iletişime geçeceğiz.

Saygılarımızla,
Randevu Sistemi
"""
            mail.send(msg)
        except Exception as e:
            print(f"Mail gönderme hatası: {e}")

        return render_template('index.html', 
            success_message=f'Randevunuz başarıyla oluşturuldu! Randevu ID: {yeni_randevu.id}. Bilgilendirme e-postası gönderildi.')
    
    except Exception as e:
        db.session.rollback()
        return render_template('index.html', 
            error_message=f'Bir hata oluştu: {str(e)}')

# Admin API - Tüm Randevuları Görüntüle
@app.route('/api/randevular')
def api_randevular():
    randevular = Randevu.query.order_by(Randevu.olusturma_tarihi.desc()).all()
    return jsonify([r.to_dict() for r in randevular])

# API - Belirli Bir Randevuyu Al
@app.route('/api/randevular/<int:id>')
def api_randevu_detay(id):
        randevu = Randevu.query.get_or_404(id)
    return jsonify(randevu.to_dict())

# API - Randevu Durumunu Güncelle
@app.route('/api/randevular/<int:id>/durum', methods=['POST'])
def api_randevu_durum_guncelle(id):
    randevu = Randevu.query.get_or_404(id)
    data = request.get_json()
    
    if 'durum' in data:
        randevu.durum = data['durum']
        db.session.commit()
        return jsonify({'success': True, 'message': 'Durum güncellendi'})
    
    return jsonify({'success': False, 'message': 'Durum parametresi gerekli'}), 400

# API - Randevu Sil
@app.route('/api/randevular/<int:id>', methods=['DELETE'])
def api_randevu_sil(id):
    randevu = Randevu.query.get_or_404(id)
    db.session.delete(randevu)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Randevu silindi'})

# İstatistikler
@app.route('/api/istatistikler')
def api_istatistikler():
    toplam = Randevu.query.count()
    onay_beklemede = Randevu.query.filter_by(durum='Onay Beklemede').count()
    onayland = Randevu.query.filter_by(durum='Onaylandı').count()
    iptal = Randevu.query.filter_by(durum='İptal').count()
    
    hizmet_dagilimi = {}
    randevular = Randevu.query.all()
    for r in randevular:
        hizmet_dagilimi[r.hizmet] = hizmet_dagilimi.get(r.hizmet, 0) + 1
    
    return jsonify({
        'toplam': toplam,
        'onay_beklemede': onay_beklemede,
        'onayland': onayland,
        'iptal': iptal,
        'hizmet_dagilimi': hizmet_dagilimi
    })

# Sağlık Kontrolü
@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'message': 'Randevu sistemi çalışıyor'})

# Hata Sayfaları
@app.errorhandler(404)
def sayfa_bulunamadi(error):
    return render_template('index.html', 
        error_message='Aradığınız sayfa bulunamadı.'), 404

@app.errorhandler(500)
def sunucu_hatasi(error):
    db.session.rollback()
    return render_template('index.html', 
        error_message='Sunucu hatası oluştu. Lütfen daha sonra tekrar deneyin.'), 500

# Vercel uyumluluğu için
if __name__ == '__main__':
    # Geliştirme ortamı
    app.run(debug=True, host='0.0.0.0', port=5000)

# Vercel production
app.run = lambda: None
