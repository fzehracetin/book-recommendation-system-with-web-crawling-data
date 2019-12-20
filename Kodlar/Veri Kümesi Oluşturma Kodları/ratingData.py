import pandas as pd
import matplotlib.pyplot as plt
import csv
import io
import random as r

users = pd.read_csv('user_data.csv', sep=',', error_bad_lines=False, encoding="utf-8")
users.columns = ['User Id', 'Yas', 'Cinsiyet']

books = pd.read_csv('book_file.csv', sep=',', error_bad_lines=False, encoding="utf-8")
books.columns = ['Adı', 'Yazar', 'Alt başlık', 'Baskı tarihi', "Sayfa sayısı", "Format", "ISBN", "Kitabın türü", "Orijinal adı",
                  "Çeviri", "Dil", "Ülke", "Yayınevi", "Baskılar", "Yaş", "Cinsiyet", "Puan", "Oy Sayısı"]
# print(list(users.columns))

users.head()

with io.open('rating_data.csv', mode='w', encoding="utf-8") as rating_file:
    fieldnames = ['User Id', 'ISBN', 'Puan']
    rating_writer = csv.DictWriter(rating_file, fieldnames=fieldnames)
    rating_writer.writeheader()

    rating_dict = {
        "User Id": "null",
        "ISBN": "0",
        "Puan": "null"
    }

    for i in range(1, 1001):

        rating_dict["User Id"] = i
        index = r.sample(range(1, 1000), 100)
        index.sort()
        for j in range(100):
            rating_dict["ISBN"] = books["ISBN"][index[j]]
            ort_puan = books["Puan"][index[j]]

            alt_sinir = int(ort_puan) - 3
            ust_sinir = int(ort_puan) + 3

            if int(ort_puan) < 3:
                alt_sinir = 0
            if int(ort_puan) > 7:
                ust_sinir = 10

            ort_puan = r.randint(alt_sinir, ust_sinir)
            rating_dict["Puan"] = ort_puan

            rating_writer.writerow(rating_dict)


