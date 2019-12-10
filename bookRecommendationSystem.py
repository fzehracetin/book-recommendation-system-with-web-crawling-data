import requests
import re
from bs4 import BeautifulSoup


def hesapla(text):
    firstDelPos = text.find("(")  # get the position of [
    secondDelPos = text.find(")")  # get the position of ]
    stringAfterReplace = text.replace(text[firstDelPos :secondDelPos + 1], " ")
    print (stringAfterReplace) # print the string after sub string between dels is replaced
    # print(text)
    return text

for i in range(1,41):
    print(i)
    main_url = "https://1000kitap.com/kitaplar?s=en-cok-okunanlar&sayfa=" + str(i)

    r = requests.get(main_url)

    soup = BeautifulSoup(r.content, "html.parser")

    gelen_veri = soup.find_all("div", {"class": "ana-liste"})

    kitap_listesi = (gelen_veri[0].contents)[0]

    kitap_listesi = kitap_listesi.find_all("li", {"class": "kitap butonlu"})

    for kitap in kitap_listesi:
        link = requests.get(kitap.a.get('href'))
        soup2 = BeautifulSoup(link.content, "html.parser")

        ana_sag = soup2.find("div", {"class": "ana-sag"})
        kutu_bilgiler = ana_sag.find("div", {"class": "kutu bilgiler"})
        j = 0
        for d in kutu_bilgiler:

            # if d.name == 'div':
                #print(d.text)
            if j == 9:
                break
            j = j+1
        j=0
        for d in ana_sag:
            if d.name == 'div' and d.get('class', '') == ['kutu']:
                # print(d.text)
                if j == 2:
                    text = hesapla(d.text)
                j = j + 1

