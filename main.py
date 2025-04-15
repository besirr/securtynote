import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import base64


def sifrele(metin, key):
    try:
        metin = metin.encode("utf-8")
        key = key.encode("utf-8")
        encoded = base64.b64encode(metin + key).decode("utf-8")
        return encoded
    except Exception as e:
        return str(e)


def coz(metin, key):
    try:
        decoded = base64.b64decode(metin).decode("utf-8")
        if decoded.endswith(key):
            return decoded[:-len(key)]
        else:
            return "Hatalı şifre!"
    except:
        return "Çözümleme başarısız!"


def kaydet():s
    baslik = my_baslik_entry.get()
    icerik = my_password_entry.get("1.0", tkinter.END).strip()
    sifre = my_key_entry.get()

    if baslik == "" or icerik == "" or sifre == "":
        messagebox.showwarning("Uyarı", "Tüm alanları doldurun!")
        return

    sifreli = sifrele(icerik, sifre)

    with open("notlar.txt", "a", encoding="utf-8") as dosya:
        dosya.write(f"Başlık: {baslik}\n")
        dosya.write(f"Not: {sifreli}\n")
        dosya.write("-" * 30 + "\n")

    my_baslik_entry.delete(0, tkinter.END)
    my_password_entry.delete("1.0", tkinter.END)
    my_key_entry.delete(0, tkinter.END)
    messagebox.showinfo("Başarılı", "Not kaydedildi (şifrelenmiş olarak).")


def goster():
    metin = my_password_entry.get("1.0", tkinter.END).strip()
    sifre = my_key_entry.get()

    if metin == "" or sifre == "":
        messagebox.showwarning("Uyarı", "Şifreli metin ve anahtar girilmeli!")
        return

    sonuc = coz(metin, sifre)
    my_password_entry.delete("1.0", tkinter.END)
    my_password_entry.insert(tkinter.END, sonuc)



window = tkinter.Tk()
window.title("Gizli Not Uygulaması")
window.minsize(450, 650)

img = Image.open("securty.webp")
img = img.resize((200, 200))
photo = ImageTk.PhotoImage(img)
label = tkinter.Label(window, image=photo)
label.pack()

tkinter.Label(text="Şifre adı nedir", font=('arial', 10, "normal")).pack()
my_baslik_entry = tkinter.Entry(width=25)
my_baslik_entry.pack()

tkinter.Label(text="Notunuz", font=('arial', 10, "normal")).pack()
my_password_entry = tkinter.Text(width=35, height=10)
my_password_entry.pack()

tkinter.Label(text="Anahtar", font=('arial', 10, "normal")).pack()
my_key_entry = tkinter.Entry(width=25, show="*")
my_key_entry.pack()

tkinter.Button(text="Kaydet", command=kaydet).pack(pady=5)
tkinter.Button(text="Göster", command=goster).pack()

window.mainloop()
