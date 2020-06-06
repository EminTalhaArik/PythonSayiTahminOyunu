# -*- coding: utf-8 -*-

import random

macDevam = False

def nasilOynanir():
    print("---------------------------")
    print("1 - Sayı Küçüktür Uyarısı Alırsanız Daha Büyük Bir Tahminde Bulunun.")
    print("2 - Sayı Büyüktür Uyarısı Alırsanız Daha Küçük Bir Tahminde Bulunun.")
    print("3 - Oyuna Başla Seçeneği İle Oyuna Başlayabilirsiniz.")
    print("4 - Oyunda Hak Sistemi Yoktur. İstediğiniz Kadar Tahminde Bulunabilirsiniz.")
    print("---------------------------")

tahminEdilecekSayi = random.randint(1,100)

oyunDevam = True


print("=============Sayı Tahmin Oyunu============= \n")

while oyunDevam == True:
    

    print("1 - Oyuna Başla , 2 - Nasıl Oynanır? , 0 - Çıkış Yap")
    
    secim = int(input("Lütfen Bir Seçim Yapınız : "))
    
    if secim == 1:
        print("------------------------")
        print("Oyun Başladı")
        print("------------------------")
        macDevam = True

    elif secim == 2:
        nasilOynanir()
    elif secim == 0:
        print("Oyundan Çıkış Yapılıyor.")
        oyunDevam = False
    else:
        print("Yanlış Veri Girişi")
    
    while macDevam:
        
        tahmin = int(input("Lütfen Bir Tahminde Bulunun : "))
        print("\n")
        
        if tahmin == tahminEdilecekSayi:
            print("---------------------------")
            print("Tebrikler Doğru Bildiniz!")
            print("---------------------------")
            macDevam = False
        
        elif tahmin < tahminEdilecekSayi:
            print("---------------------------")
            print("Biraz Daha Büyük Tahminde Bulunun")
            print("---------------------------")
            
        elif tahmin > tahminEdilecekSayi:
            print("---------------------------")
            print("Biraz Daha Küçük Tahminde Bulunun")
            print("---------------------------")
            
        else:
            print("!!!!!!!!!!!!!!!!!!!!!")
            print("Yanlış Veri Girişi")
            print("!!!!!!!!!!!!!!!!!!!!!")
            macDevam = False
            