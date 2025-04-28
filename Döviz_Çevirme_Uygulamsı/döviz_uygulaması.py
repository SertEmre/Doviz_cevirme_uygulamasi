import requests

api_key = "45d15eb138fbf96cfa53fd76"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

def doviz_cevir():

    bozulan_döviz = input("Bozulan döviz türü: ").upper()
    alinan_döviz = input("Alınan döviz türü: ").upper()
    miktar = float(input(f"Ne kadar {bozulan_döviz} bozdurmak istiyorsunuz?: "))

    sonuc = requests.get(api_url + bozulan_döviz)

    if sonuc.status_code == 200:
        sonuc_json = sonuc.json()
        try:
            print("{0} {1} = {2} {3} ".format(miktar,bozulan_döviz,miktar*sonuc_json["conversion_rates"][alinan_döviz],alinan_döviz ))
        except KeyError:
            print("Hatalı döviz türü girdiniz.")
    else:
        print("API isteği başarısız oldu.")

def kurları_göster():
    istenen_döviz = input("Hangi dövizin kurlarını görmek istersiniz?: ").upper()
    response = requests.get(api_url + istenen_döviz)

    if response.status_code == 200:
        data = response.json()
        for doviz, oran in list(data["conversion_rates"].items()):
            print(f"{istenen_döviz} = {doviz}{oran}")
    else:
        print("API alınırken bir sorun oldu.")

def menü():
    while True:
        print("-"*20 + "Döviz İşlemleri Menüsü" + "-"*20)
        print("1-Döviz Çevirme")
        print("2-Kurları Görüntüle")
        print("3-Çıkış yap")
        secim = input("Lütfen bir seçim yapınız: ")

        if secim == "1":
            doviz_cevir()
        elif secim == "2":
            kurları_göster()
        elif secim == "3":
            print("Çıkış yapıldı.")
            break
        else:
            print("Geçersiz seçim yaptınız.Tekrar deneyiniz.")

if __name__ == "__main__":
    menü()
