import tkinter as tk
from tkinter import messagebox
import os

pencere = tk.Tk()
pencere.title("Mini Sosyal Medya Uygulaması")
pencere.geometry("350x450")
pencere.config(bg="#f0f2f5") 

# Kayıt olan kullanıcıları saklayacağımız global sözlük
kullanıcı_söz = {}

# Uygulama ilk açıldığında dosyadan kayıtlı kullanıcıları hafızaya yükle
if os.path.exists("sifreler.txt"):
    with open("sifreler.txt", "r", encoding="utf-8") as dosya:
        for satir in dosya.readlines():
            parcalar = satir.strip().split(":")
            if len(parcalar) == 2:
                kullanıcı_söz[parcalar[0]] = parcalar[1]

def ekranı_temizle():
    for widget in pencere.winfo_children():
        widget.destroy()

# ==========================================
# 1. GİRİŞ EKRANI
# ==========================================
def giriş_ekranı():
    ekranı_temizle()
    
    tk.Label(pencere, text="Giriş Paneli", font=("Arial", 14, "bold"), bg="#f0f2f5", fg="#333").pack(pady=15)

    tk.Label(pencere, text="Kullanıcı Adı:", font=("Arial", 10, "bold"), bg="#f0f2f5").pack(pady=(10, 2))
    giris_ad = tk.Entry(pencere, width=28, font=("Arial", 10))
    giris_ad.pack(pady=5)

    tk.Label(pencere, text="Şifre:", font=("Arial", 10, "bold"), bg="#f0f2f5").pack(pady=(10, 2))
    giris_sifre = tk.Entry(pencere, width=28, font=("Arial", 10), show="*")
    giris_sifre.pack(pady=5)
    
    durum_lbl = tk.Label(pencere, text="", font=("Arial", 9, "bold"), bg="#f0f2f5")
    durum_lbl.pack(pady=10)

    def kontrol_et():
        kadi = giris_ad.get()
        sifre = giris_sifre.get()
        
        if kadi in kullanıcı_söz and kullanıcı_söz[kadi] == sifre:
            messagebox.showinfo("Başarılı", "Giriş Başarılı!")
            # Başarılı girişten sonra akış ekranına yönlendiriyoruz!
            akış_ekranı(kadi)
        else:
            messagebox.showerror("Hata", "Kullanıcı adı veya şifre hatalı!")
            durum_lbl.config(text="Hatalı giriş!", fg="red")

    tk.Button(pencere, text="Giriş Yap", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", width=15, command=kontrol_et).pack(pady=10)
    tk.Button(pencere, text="Hesabın yok mu? Kayıt Ol", bg="#dee3e5", fg="#007BFF", bd=0, font=("Arial", 9, "underline"), command=kayıt_ekranı).pack(pady=5)

# ==========================================
# 2. KAYIT OLMA EKRANI
# ==========================================
def kayıt_ekranı():
    ekranı_temizle()
    
    tk.Label(pencere, text="Kayıt Ol", font=("Arial", 14, "bold"), bg="#f0f2f5", fg="#333").pack(pady=15)

    tk.Label(pencere, text="Kullanıcı Adı:", font=("Arial", 10, "bold"), bg="#f0f2f5").pack(pady=(10, 2))
    yeni_ad = tk.Entry(pencere, width=28, font=("Arial", 10))
    yeni_ad.pack(pady=5)

    tk.Label(pencere, text="Şifre:", font=("Arial", 10, "bold"), bg="#f0f2f5").pack(pady=(10, 2))
    yeni_sifre = tk.Entry(pencere, width=28, font=("Arial", 10), show="*")
    yeni_sifre.pack(pady=5)

    tk.Label(pencere, text="Şifre Tekrar:", font=("Arial", 10, "bold"), bg="#f0f2f5").pack(pady=(10, 2))
    yeni_sifre_tekrar = tk.Entry(pencere, width=28, font=("Arial", 10), show="*")
    yeni_sifre_tekrar.pack(pady=5)
    
    durum_lbl = tk.Label(pencere, text="", font=("Arial", 9, "bold"), bg="#f0f2f5")
    durum_lbl.pack(pady=10)

    def verileri_al():
        alinan_kadi = yeni_ad.get()
        alinan_sifre = yeni_sifre.get()
        alinan_sifre_tekrar = yeni_sifre_tekrar.get()
        
        if len(alinan_sifre) < 1 or len(alinan_kadi) < 1:
            durum_lbl.config(text="Alanlar boş bırakılamaz!", fg="red")
        elif alinan_sifre_tekrar != alinan_sifre:
            durum_lbl.config(text="Şifreler eşleşmiyor!", fg="red")
            yeni_sifre_tekrar.delete(0, "end")
            yeni_sifre.delete(0, "end")
        elif alinan_kadi in kullanıcı_söz:
            durum_lbl.config(text="Bu kullanıcı adı zaten alınmış!", fg="red")
        else:
            # Sözlüğe kaydet
            kullanıcı_söz[alinan_kadi] = alinan_sifre
            
            # Dosyaya da kalıcı olarak yaz
            with open("sifreler.txt", "a", encoding="utf-8") as dosya:
                dosya.write(f"{alinan_kadi}:{alinan_sifre}\n")
                
            messagebox.showinfo("Başarılı", "Kayıt Başarıyla Oluşturuldu!")
            giriş_ekranı()
            
    tk.Button(pencere, text="Kaydet", font=("Arial", 10, "bold"), bg="#ff9800", fg="white", width=15, command=verileri_al).pack(pady=10)
    tk.Button(pencere, text="Zaten hesabın var mı? Giriş Yap", bg="#f0f2f5", fg="#007BFF", bd=0, font=("Arial", 9, "underline"), command=giriş_ekranı).pack(pady=5)

# ==========================================
# 3. AKIŞ EKRANI (SOSYAL MEDYA PANELİ)
# ==========================================
def akış_ekranı(aktif_kullanici): 
    ekranı_temizle()
    
    # Üst Bilgi
    tk.Label(pencere, text=f"Hoş Geldin, {aktif_kullanici}", font=("Arial", 12, "bold"), bg="#f0f2f5", fg="#333").pack(pady=10)
    tk.Label(pencere, text="Ne düşünüyorsun?", font=("Arial", 10), bg="#f0f2f5").pack()
    
    # Çok satırlı gönderi kutusu (height ve width düzeltildi)
    gönderi_kutusu = tk.Text(pencere, width=32, height=5, font=("Arial", 10))
    gönderi_kutusu.pack(pady=5)
    
    def gönderiyi_kaydet():
        metin = gönderi_kutusu.get("1.0", "end").strip()
        if len(metin) > 0:
            with open("gonderiler.txt", "a", encoding="utf-8") as g_dosya:
                g_dosya.write(f"{aktif_kullanici}: {metin}\n")
            messagebox.showinfo("Başarılı", "Gönderi paylaşıldı!")
            gönderi_kutusu.delete("1.0", "end")
        else:
            messagebox.showwarning("Uyarı", "Boş gönderi paylaşılamaz!")

    tk.Button(pencere, text="Paylaş", bg="#007BFF", fg="white", font=("Arial", 10, "bold"), width=15, command=gönderiyi_kaydet).pack(pady=5)
    
    # Çıkış Yap Butonu
    tk.Button(pencere, text="Çıkış Yap", bg="#f44336", fg="white", font=("Arial", 9), width=10, command=giriş_ekranı).pack(pady=10)

# Uygulamayı başlat
giriş_ekranı()
pencere.mainloop()
