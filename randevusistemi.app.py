from flask import Flask, render_template, request

app = Flask(_name_)

# Örnek veritabanı (Gerçek uygulamada SQL kullanılır)
randevular = []

@app.route('/', methods=['GET', 'POST'])
def ana_sayfa():
    bildirim = None
    
    if request.method == 'POST':
        # Formdan gelen verileri al
        ad = request.form.get('ad')
        email = request.form.get('email')
        tarih = request.form.get('tarih')
        bolum = request.form.get('bolum')
        
        # Veriyi kaydet
        yeni_randevu = {
            'ad': ad, 
            'email': email, 
            'tarih': tarih, 
            'bolum': bolum
        }
        randevular.append(yeni_randevu)
        
        # Başarı mesajı gönder
        bildirim = f"Teşekkürler {ad}, {bolum} bölümü için randevunuz ({tarih}) oluşturuldu!"

    return render_template('index.html', bildirim=bildirim)

if _name_ == '_main_':
    app.run(debug=True)