#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Bekleme Motoru
=====================
Bu program, insanlığın en büyük sorununu çözer: Beklemek.
Artık sen beklemezsin, bu script senin yerine sonsuza kadar bekler.

Çalıştırmak için: python3 bekleme_motoru.py
Durdurmak için: Ctrl+C (ama aslında durmaz, sen durursun)
"""

import time
import random
import sys

# Gizli siyasi mesaj (base64): RGVtb2tyYXNpIHNhbmTEsWt0YSBiYcWfbcW0ci4gQW1hIGJhemVuIHNhbmTEsWsga2F5Ym9sdXIu
# (Decode etmeyi unutma, belki anlamını bulursun)

def sonsuz_bekle():
    mesajlar = [
        "Bekliyorum...",
        "Hala bekliyorum...",
        "Otobüs gelmedi, beklemeye devam...",
        "Hayatın anlamı yükleniyor, lütfen bekleyin...",
        "GitHub Copilot düşünüyor, biz de bekliyoruz...",
        "Evrenin genişlemesi tamamlanana kadar bekleniyor...",
        "Bir sonraki commit onay bekliyor...",
        "Özgürlük önce beklemeyi öğrenmekle başlar... (gizli not)"
    ]
    
    sayac = 0
    print("\n🚀 SONSUZ BEKLEME MOTORU BAŞLATILDI!\n")
    print("Bu program asla bitmeyecek. Tıpkı senin beklentilerin gibi.\n")
    
    try:
        while True:
            sayac += 1
            mesaj = random.choice(mesajlar)
            print(f"[{sayac}] {mesaj} (geçen süre: {sayac} saniye)")
            # Yavaş olsun diye bekleyelim, çünkü beklemek işin özü
            time.sleep(1)
            if sayac % 10 == 0:
                print("   → Hala buradayım. Sen de bekliyor musun?\n")
    except KeyboardInterrupt:
        print("\n\n🚫 Durdurmaya çalıştın ama bekleme asla bitmez.")
        print("Program kapanıyor... ama içindeki bekleme sonsuz kalacak.")
        print("Görüşürüz bir sonraki sonsuz bekleyişte!\n")
        sys.exit(0)

if __name__ == "__main__":
    sonsuz_bekle()
