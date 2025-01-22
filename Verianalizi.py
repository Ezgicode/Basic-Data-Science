
#Bütün gerekli  kütüphaneleri içeri aktarıyoruz.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

#Python uyarıları kapatıyoruz
import warnings
warnings.filterwarnings("ignore")


# Dosyanın tam yolunu gir
veri = pd.read_csv(r"C:\Users\ezgii\OneDrive\Masaüstü\DataSet\4_Veri_Bilimi_Görselleştirme\olimpiyatlar.csv")

#Veri hakkında bilgi almak için
veri.info()


# İlk 5 satırı görüntüle
print("İlk 2 satır:")
print(veri.head(2))

# Sütunların adlarını yazdır
print("\nSütunlar:")
print(veri.columns)


veri.rename(columns={'ID'  : 'id',
                     'Name'  :'isim',
                     'Height' :'boy',
                     'Weight' : 'kilo',
                     }, inplace= True)


# Drop fonksiyonu ile id sütununu çıkaralım axis= 1 sütunu temsil eder.
veri = veri.drop(["id"], axis=1)

# Eksik değerleri kontrol et
print("\nEksik Değerler:")
#print(df.isnull().sum())


essiz_etkinlik = pd.unique(veri.Event)
print(" Eşsiz etkinlik sayısı:{} ".format(len(essiz_etkinlik)))
print(essiz_etkinlik[:10])

#Her bir etkinliği iteratif olarak dolaş
#etkinlik özelinde boy ve kilo ortalamalarını hesapla
#etkinlik özelinde kayıp boy ve kilo değerlerini etkinlik ortalamalarına eşitle
veri_gecici = veri.copy() # gerçek veriyi bozmamak için kopyasını oluşturuyoruz
boy_kilo_liste = ["boy", "kilo"]

# Önce etkinlik filtresi oluşturduk sonra veriyi etkinliğe göre filtreledik
for e in essiz_etkinlik :
    etkinlik_filtre = veri_gecici.etkinlik == e
    veri_filtreli = veri_gecici[etkinlik_filtre] 

# boy ve kilo için  etkinlik özelinde ortalamaları hesaplıyor
    for s in boy_kilo_liste :
        ortalama = np.round(np.mean(veri_filtreli[s]),2)
        if ~np.isnan(ortalama):
            veri_filtreli[s] = veri_filtreli[s].fillna(ortalama)
        else:
            tum_veri_ortalaması = np.round(np.mean(veri[s]),2)
            veri_filtreli[s] = veri_filtreli[s].fillna(tum_veri_ortalaması)
            
veri_gecici[etkinlik_filtre] = veri_filtreli

veri = veri_gecici.copy()
veri.info()

# Yaş değişkeninde tanımlı olmayan değerleri buluyoruz
yas_ortalaması = np.round(np.mean(veri.yas),2)
print("Yaş ortalaması :{}".format(yas_ortalaması))
veri["yaş"] = veri["yaş"].fillna(yas_ortalaması)
veri.info

#Madalya alamayan sporcuları veri setinden çıkaracağız
madalya_degiskeni = veri["madalya"]
pd.isnull(madalya_degiskeni).sum()

madalya_degiskeni_filtresi = pd.isnull(madalya_degiskeni)

veri = veri[madalya_degiskeni_filtresi]
veri.head(5)
veri.info()

#Sonradan kullanabilmek için veriyi kaydediyoruz
veri.to_csv("olimpiyatlar_temizlenmiş_csv", index =False)






        
        
        
        
        
        
        
        
        
        
        