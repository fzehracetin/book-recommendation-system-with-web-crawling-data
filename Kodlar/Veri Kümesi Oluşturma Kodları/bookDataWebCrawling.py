import requests
from bs4 import BeautifulSoup
import csv
import io
import re


def hesapla (text):
    print(text)
    while (text.find("(") != -1):
        firstDelPos = text.find("(")  # get the position of [
        secondDelPos = text.find(")")  # get the position of ]
        text = text.replace(text[firstDelPos :secondDelPos + 1], " ")
    a = text.split("  ")
    # print(a)
    puan = 0
    for i in range(0, len(a) - 1):
        x = a[i].split("%")
        # print(x)
        #print(float(x[0]) * float(x[1]) / 100)
        puan = puan + float(x[0]) * float(x[1]) / 100
        # print(puan)
    # print(puan)
    return puan


with io.open("book_file5.csv", mode='w', encoding="utf-8") as book_file:
    fieldnames = ['Adı', 'Yazar', 'Alt başlık', 'Baskı tarihi', "Sayfa sayısı", "Format", "ISBN", "Kitabın türü", "Orijinal adı",
                  "Çeviri", "Dil", "Ülke", "Yayınevi", "Baskılar", "Yaş", "Cinsiyet", "Puan", "Oy Sayısı"]
    book_writer = csv.DictWriter(book_file, fieldnames=fieldnames)
    book_writer.writeheader()

    for i in range(36, 41):
        print(i)
        main_url = "https://1000kitap.com/kitaplar?s=en-cok-okunanlar&sayfa=" + str(i)

        r = requests.get(main_url)

        soup = BeautifulSoup(r.content, "html.parser")

        gelen_veri = soup.find_all("div", {"class": "ana-liste"})

        kitap_listesi = gelen_veri[0].contents[0]

        kitap_listesi = kitap_listesi.find_all("li", {"class": "kitap butonlu"})

        for kitap in kitap_listesi:
            book_dict = {
                "Adı": "null",
                "Yazar": "null",
                'Alt başlık': "null",
                "Baskı tarihi": "null",
                "Sayfa sayısı": "0",
                "Format": "null",
                "ISBN": "0",
                "Kitabın türü": "null",
                "Orijinal adı": "null",
                "Çeviri": "null",
                "Dil": "null",
                "Ülke": "null",
                "Yayınevi": "null",
                "Baskılar": "null",
                "Yaş": "null",
                "Cinsiyet": "null",
                "Puan": "null",
                "Oy Sayısı": "null"
            }

            metin = kitap.find("div",{"class": "bilgi ekBilgi"}).text
            metin = re.sub(r'O.*', ' ', metin)
            metin = metin.split("(")
            metin[0] = re.sub(r'/.*', ' ', metin[0])

            puan = metin[0].strip()
            oy = metin[1].strip()
            book_dict["Puan"] = puan
            book_dict["Oy Sayısı"] = oy

            link = requests.get(kitap.a.get('href'))
            soup2 = BeautifulSoup(link.content, "html.parser")

            ana_sag = soup2.find("div", {"class": "ana-sag"})
            kutu_bilgiler = ana_sag.find("div", {"class": "kutu bilgiler"})

            j = 0

            for d in kutu_bilgiler:

                if d.name == 'div':
                    text = d.text.split(":")
                    book_dict[text[0]] = text[1]
                if j == 9:
                    break
                j = j + 1
            j = 0
            for d in ana_sag:
                if d.name == 'div' and d.get('class', '') == ['kutu']:
                    if j == 0:
                        book_dict["Yaş"] = d.text
                    if j == 1:
                        book_dict["Cinsiyet"] = d.text
                    j = j + 1

            book_writer.writerow(book_dict)