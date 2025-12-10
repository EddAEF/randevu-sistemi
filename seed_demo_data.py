#!/usr/bin/env python3
"""
Demo Veri Yükleme Script'i
Veritabanına örnek randevular ekler
"""

from app import app, db, Randevu
from datetime import datetime, timedelta
import random

def demo_verileri_yukle():
    """Demo verileri yükle"""
    
    with app.app_context():
        # Eğer veritabanında veri varsa sorma
        if Randevu.query.count() > 0:
            print("⚠️  Veritabanında zaten veri var!")
            cevap = input("Üzerine yazılsın mı? (evet/hayır): ").strip().lower()
            if cevap != 'evet':
                print("İptal edildi.")
                return
            
            # Tüm veriyi sil
            Randevu.query.delete()
            db.session.commit()
            print("✓ Eski veriler silindi")
        
        # Demo veriler
        demo_randevular = [
            {
                'ad_soyad': 'Ahmet Yılmaz',
                'telefon': '+90 555 123 4567',
                'email': 'ahmet@example.com',
                'tarih': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'),
                'saat': '09:00',
                'hizmet': 'Danışmanlık',
                'konu': 'İş Danışmanlığı',
                'aciklama': 'Şirketim için danışmanlık hizmeti almak istiyorum.',
                'durum': 'Onay Beklemede'
            },
            {
                'ad_soyad': 'Fatma Kaya',
                'telefon': '+90 555 234 5678',
                'email': 'fatma@example.com',
                'tarih': (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d'),
                'saat': '10:30',
                'hizmet': 'Teknik Destek',
                'konu': 'Teknik Destek Talebi',
                'aciklama': 'Sistem hataları nedeniyle teknik destek istiyorum.',
                'durum': 'Onaylandı'
            },
            {
                'ad_soyad': 'Mehmet Çetin',
                'telefon': '+90 555 345 6789',
                'email': 'mehmet@example.com',
                'tarih': (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d'),
                'saat': '14:00',
                'hizmet': 'Raporlama',
                'konu': 'Aylık Rapor Hazırlanması',
                'aciklama': 'Aylık iş raporu için randevu almak istiyorum.',
                'durum': 'Onay Beklemede'
            },
            {
                'ad_soyad': 'Ayşe Demir',
                'telefon': '+90 555 456 7890',
                'email': 'ayse@example.com',
                'tarih': (datetime.now() + timedelta(days=4)).strftime('%Y-%m-%d'),
                'saat': '15:30',
                'hizmet': 'Güvenlik',
                'konu': 'Güvenlik Danışmanlığı',
                'aciklama': 'Şirket güvenliği konusunda danışmanlık almak istiyorum.',
                'durum': 'İptal'
            },
            {
                'ad_soyad': 'Can Yıldız',
                'telefon': '+90 555 567 8901',
                'email': 'can@example.com',
                'tarih': (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d'),
                'saat': '11:00',
                'hizmet': 'Proje Yönetimi',
                'konu': 'Yeni Proje Planlama',
                'aciklama': 'Yeni bir projenin yönetimi için danışmanlık istiyorum.',
                'durum': 'Onaylandı'
            },
            {
                'ad_soyad': 'Elif Şahin',
                'telefon': '+90 555 678 9012',
                'email': 'elif@example.com',
                'tarih': (datetime.now() + timedelta(days=6)).strftime('%Y-%m-%d'),
                'saat': '09:30',
                'hizmet': 'Müşteri Hizmetleri',
                'konu': 'Müşteri Hizmetleri Eğitimi',
                'aciklama': 'Ekibim için müşteri hizmetleri eğitimi istiyorum.',
                'durum': 'Onay Beklemede'
            }
        ]
        
        # Verileri ekle
        for veri in demo_randevular:
            randevu = Randevu(
                ad_soyad=veri['ad_soyad'],
                telefon=veri['telefon'],
                email=veri['email'],
                tarih=veri['tarih'],
                saat=veri['saat'],
                hizmet=veri['hizmet'],
                konu=veri['konu'],
                aciklama=veri['aciklama'],
                durum=veri['durum']
            )
            db.session.add(randevu)
        
        # Kaydet
        db.session.commit()
        
        print("✓ Demo verileri başarıyla yüklendi!")
        print(f"✓ {len(demo_randevular)} randevu eklendi")
        print("\n📊 İstatistikler:")
        print(f"   Toplam: {Randevu.query.count()}")
        print(f"   Onay Beklemede: {Randevu.query.filter_by(durum='Onay Beklemede').count()}")
        print(f"   Onaylandı: {Randevu.query.filter_by(durum='Onaylandı').count()}")
        print(f"   İptal: {Randevu.query.filter_by(durum='İptal').count()}")
        print("\n🌐 Admin paneli: http://localhost:5000/admin")

if __name__ == '__main__':
    print("🎯 Randevu Sistemi - Demo Veri Yükleme")
    print("=" * 40)
    demo_verileri_yukle()
