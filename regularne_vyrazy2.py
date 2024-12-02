import re
import requests

link = "https://auto.bazos.cz/"
stranka = requests.get(link)

vyraz = r"/inzerat[A-Za-z0-9/-]*"
odkazy = re.findall(vyraz, stranka.text)

for odkaz in odkazy:
    odkaz_full = link + odkaz
    print(odkaz_full)
    stranka_inzeratu = requests.get(odkaz_full)


    skratky = re.findall(r"(\d{1,6})\s?km", stranka_inzeratu.text)
    for skratka in skratky:
        print(f" {skratka} km")


    vsechen_text = re.findall(r"<p[^>]*>(.*?)</p>", stranka_inzeratu.text, re.DOTALL)
    for text in vsechen_text:
        print(f"Obsah odseku: {text.strip()}")