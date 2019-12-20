import io
import csv
import random as r


with io.open("user_data.csv", mode='w', encoding="utf-8") as user_file:
    fieldnames = ['User Id', 'Yas', 'Cinsiyet']
    user_writer = csv.DictWriter(user_file, fieldnames=fieldnames)
    user_writer.writeheader()

    usrdict = {
        "User Id": "null",
        "Yas": "null",
        "Cinsiyet": "null"
    }

    for i in range(1, 1001):

        usrdict["User Id"] = i
        if r.randint(0, 100) < 11:
            usrdict["Yas"] = "null"
        else:
            usrdict["Yas"] = r.randint(17, 70)
        if r.randint(0, 100) < 11:
            usrdict["Cinsiyet"] = "null"
        else:
            cinsiyet = r.randint(0, 2)
            if cinsiyet == 1:
                usrdict["Cinsiyet"] = "K"
            else:
                usrdict["Cinsiyet"] = "E"

        user_writer.writerow(usrdict)