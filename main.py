import time
from dataURL import DataURL
from getURL import GetURL

useDataURL = DataURL()
useGetURL = GetURL()

print("-:Mini Örümceğe hoş geldiniz! -_- ")
print("|---------------------------------------------------------|")
kullanıcı = input("Adınızı giriniz:")
print( "Merhaba " + kullanıcı  +  " Mini örümcek başlatılıyor...")
print("")
time.sleep(2)

while True:
    print("Menü: 0)Çıkış 1)URL Listele 2)URL Ekle 3)Örümcek Gönder 4)Sonuçları Listele")
    print("Sadece seçiminizin önündeki rakamı giriniz.")
    menuSecim = int(input("Seçiminiz: "))
    if menuSecim == 0:
        print("Mini Örümcek kapatılıyor...")
        time.sleep(1)
        break
    elif menuSecim == 1:
        useDataURL.dataRead()
    elif menuSecim == 2:
        useDataURL.dataWrite()
    elif menuSecim == 3:
        useGetURL.getWeb()
    elif menuSecim == 4:
        useGetURL.getList()
    elif menuSecim >= 4:
        print("Seçiminiz 0 ile 4 arasında değil. Tekrar seçim yapın.")

