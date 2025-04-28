import requests
import json

api_key = "45d15eb138fbf96cfa53fd76"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_döviz = input("Bozulan döviz türü: ").upper()
alinan_döviz = input("Alınan döviz türü: ").upper()
miktar = float(input(f"Ne kadar {bozulan_döviz} bozdurmak istiyorsunuz?: "))

sonuc = requests.get(api_url + bozulan_döviz)

if sonuc.status_code == 200:
    sonuc_json = json.loads(sonuc.text)
    try:
        print("{0} {1} = {2} {3} ".format(miktar,bozulan_döviz,miktar*sonuc_json["conversion_rates"][alinan_döviz],alinan_döviz ))
    except KeyError:
        print("Hatalı döviz türü girdiniz.")
else:
    print("API isteği başarısız oldu.")

