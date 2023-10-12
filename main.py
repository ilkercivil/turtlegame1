import turtle
import random
import time

# Pencere oluşturma
wn = turtle.Screen()
wn.title("Sürekli Hareket Eden Kaplumbağa Oyunu")
wn.bgcolor("white")
wn.setup(width=800, height=600)

# Kaplumbağa oluşturma
kaplumbağa = turtle.Turtle()
kaplumbağa.shape("turtle")
kaplumbağa.penup()
kaplumbağa.speed(0)

# Puan
puan = 0

# Oyun süresi (saniye cinsinden)
oyun_suresi = 30

# Hareket fonksiyonu
def hareket_et():
    x = random.randint(-380, 380)
    y = random.randint(-280, 280)
    kaplumbağa.goto(x, y)

    # Oyun süresi boyunca sürekli hareket et
    wn.ontimer(hareket_et, 1000)

# Tıklama fonksiyonu
def tıklama(x, y):
    global puan
    distance = kaplumbağa.distance(x, y)

    if distance < 20:
        puan += 1
        print("Puan:", puan)

# Tıklamaları dinle
wn.onclick(tıklama)

# Kaplumbağa hareketini başlat
hareket_et()

# Oyun zamanlayıcı
zamanlayıcı = time.time() + oyun_suresi

while time.time() < zamanlayıcı:
    wn.update()

# Oyun bittiğinde sonucu göster
sonuc = turtle.Turtle()
sonuc.color("black")
sonuc.penup()
sonuc.hideturtle()
sonuc.goto(0, 0)
sonuc.write("OYUN BİTTİ! Puanınız: {}".format(puan), align="center", font=("Arial", 24, "normal"))

wn.mainloop()
