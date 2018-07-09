from src.errorHandler import try_int, try_str, try_datum, try_vreme, try_datum_bez
from src.projekcije import uzmi_projekcije, format_projekciju
import datetime


def pretraga():
    projekcije = uzmi_projekcije()

    while True:
        print("\n")
        print("------ Pretraga ------")
        print("-" * 50)
        print("1. Pretraga po ID")
        print("-" * 50)
        print("2. Pretraga po broju sale")
        print("-" * 50)
        print("3. Pretraga po Datumu")
        print("-" * 50)
        print("4. Pretraga po Nazivu/Zanru")
        print("-" * 50)
        print("5. Povratak na glavni meni")
        print("-" * 50)
        izbor = try_int("Unesite vas izbor: ")

        if izbor == "1":
            pretraga_generic(projekcije, "ID")
        elif izbor == "2":
            pretraga_generic(projekcije, "Sala")
        elif izbor == "3":
            pretraga_generic(projekcije, "Datum")

        elif izbor == "4":
            print("-" * 50)
            unos = try_str("Unesite Naziv ili Zanr projekcije: ").lower()
            for i in projekcije:
                for k, v in i.items():
                    if k == "Naziv" or k == "Zanr":
                        if i[k].lower().__contains__(
                                unos) or i[k].lower() == unos:
                            print("-" * 50)
                            print(format_projekciju(i))
        elif izbor == "5":
            return
        else:
            print("Pogresan broj, probajte ponovo")


def pretraga_generic(projekcije, parametar):
    print("-" * 50)
    if parametar == "Datum":
        unos = try_datum("Unesite datum projekcije, format: d-m-yyyy: ")
    elif parametar == "ID":
        unos = try_str("Unesite ID projekcije: ")
    elif parametar == "Sala":
        unos = try_str("Unesite broj sale za pretragu: ")

    for i in projekcije:
        for k, v in i.items():
            if k == parametar:
                if v.lower().__contains__(unos):
                    print("-" * 50)
                    print(format_projekciju(i))


# Nacin da se sve proveri, koristi prefixe za ID i Salu

# if len(unos) <= 1:
#     print("-" * 50)
#     print("Unos ne sme biti samo jedan broj!")
#     pretraga()

# if try_datum_bez(unos):
#     for i in projekcije:
#         for k, v in i.items():
#             if k == "Datum":
#                 if v.lower().__contains__(unos):
#                     print(format_projekciju(i))

# if len(unos.split(":")) >= 2:
#     prefix = unos.split(":")[0]
#     val = unos.split(":")[1]
#     val = val.strip()
#     for i in projekcije:
#         for k, v in i.items():
#             if k.lower() == prefix:
#                 if v.lower().__contains__(val):
#                     print("-" * 50)
#                     print(format_projekciju(i))

# unos = try_str("Unesite Naziv ili Zanr projekcije: ").lower()
#             for i in projekcije:
#                 for k, v in i.items():
#                     if k == "Naziv" or k == "Zanr":
#                         if i[k].lower().__contains__(
#                                 unos) or i[k].lower() == unos:
#                             print("-" * 50)
#                             print(format_projekciju(i))