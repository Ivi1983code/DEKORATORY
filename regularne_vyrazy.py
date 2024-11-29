
import requests
import re
import time

link = "https://ct24.ceskatelevize.cz/"
stranka = requests.get(link)

vyraz = r"/clanek[A-Za-z0-9/-]*"
odkazy = re.findall(vyraz, stranka.text)

for odkaz in odkazy:
    time.sleep(0.5)
    print(link + odkaz)
    stranka = requests.get(link + odkaz)

    vsechen_text = re.findall(r"<p[^>]*>[^<]*</p>", stranka.text)

    for paragraf in vsechen_text:
        zkratky_3 = re.findall(r"\([A-Z]{3}\)", paragraf)
        zkratky_4 = re.findall(r"\([A-Z]{4}\)", paragraf)
        slova_s_velkymi_pismenami = re.findall(r"\b[A-Z][a-z]*\b", paragraf)


        for zkratka in zkratky_3:
            print(zkratka)

        for zkratka in zkratky_4:
            print(zkratka)

        for slova in slova_s_velkymi_pismenami:
            print(slova)