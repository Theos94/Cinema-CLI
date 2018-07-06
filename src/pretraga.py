from src.errorHandler import try_int, try_str, try_datum, try_vreme, try_datum_bez
from src.projekcije import uzmi_projekcije, format_projekciju
import datetime


def pretraga():
    projekcije = uzmi_projekcije()

    print("-" * 50)
    print("Pretraga je moguca po ID, Zanru, Nazivu, Sali ili Datumu")
    print(
        "Ako pretrazujete po ID ili Sali, unesite to kao prefix. Primer: ID: 2"
    )
    print("-" * 50)
    unos = try_str("Unesite parametar za pretragu: ")
    unos = unos.strip().lower()

    if len(unos) <= 1:
        print("-" * 50)
        print("Unos ne sme biti samo jedan broj!")
        pretraga()

    if try_datum_bez(unos):
        for i in projekcije:
            for k, v in i.items():
                if k == "Datum":
                    if v.lower().__contains__(unos):
                        print(format_projekciju(i))

    if len(unos.split(":")) >= 2:
        prefix = unos.split(":")[0]
        val = unos.split(":")[1]
        val = val.strip()
        for i in projekcije:
            for k, v in i.items():
                if k.lower() == prefix:
                    if v.lower().__contains__(val):
                        print("-" * 50)
                        print(format_projekciju(i))
    else:
        for i in projekcije:
            for k, v in i.items():
                if k == "Naziv" or k == "Zanr":
                    if i[k].lower().__contains__(unos):
                        print("-" * 50)
                        print(format_projekciju(i))
