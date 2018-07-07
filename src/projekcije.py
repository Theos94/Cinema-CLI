from src.errorHandler import try_int, try_str, try_datum, try_vreme
from src.filmovi import print_filmove, uzmi_filmove, format_film, dodaj_film
import datetime


def uzmi_kljuceve_proj():
    kljucevi = []

    with open("data/projekcije.txt", "r") as f:
        kljucevi = f.readline().strip().split(":")

    return kljucevi


def uzmi_projekcije():
    projekcije = []

    with open("data/projekcije.txt", "r") as f:
        kljucevi = f.readline().strip().split(":")
        for line in f.readlines():
            projekcija = dict()
            for i, v in enumerate(line.strip().split(":")):
                projekcija[kljucevi[i]] = v
            projekcije.append(projekcija)

    projekcije = sortiraj_projekcije(projekcije)
    return projekcije


def sortiraj_projekcije(projekcije):
    sorted_projekcije = sorted(projekcije, key=lambda k: k["ID"])
    return sorted_projekcije


def format_projekciju(projekcija):
    return "{ID} - {Naziv} - {Zanr} - {Cena}rsd - {Trajanje}min - {Datum} - {Pocetak} - Sala: {Sala} - {SlobodnoMesta}/{UkupnoMesta}".format(
        **projekcija)


def prikazi_projekcije():
    projekcije = uzmi_projekcije()

    for i in projekcije:
        print("-" * 100)
        print(format_projekciju(i))


def izaberi_salu():
    print(50 * "-")
    print("Sale: ")
    print("1 - 100 mesta")
    print("2 - 80 mesta")
    print("3 - 50 mesta")
    print("4 - 150 mesta")
    print("5 - 250 mesta")
    while True:
        Sala = try_int("Unesite Salu projekcije: ")
        if Sala == "1":
            return ["1", "100"]
        elif Sala == "2":
            return ["2", "80"]
        elif Sala == "3":
            return ["3", "50"]
        elif Sala == "4":
            return ["4", "150"]
        elif Sala == "5":
            return ["5", "250"]
        else:
            print("Pogresan unos, probajte ponovo")


def prikupi_inpute(idProj, izabranFilm):

    while True:

        Datum = try_datum("Unesite Datum projekcije, format - dd-m-yy: ")
        Pocetak = try_vreme("Unesite Pocetak projekcije, format - hh-mm: ")
        Cena = try_int("Unesite cenu Projekcije: ")
        Sala = izaberi_salu()

        nova_projekcija = {
            "ID": idProj,
            "Naziv": izabranFilm["Naziv"],
            "Zanr": izabranFilm["Zanr"],
            "Cena": Cena,
            "Trajanje": izabranFilm["Trajanje"],
            "Datum": Datum,
            "Pocetak": Pocetak,
            "Sala": Sala[0],
            "SlobodnoMesta": Sala[1],
            "UkupnoMesta": Sala[1]
        }

        imaMesta = proveraDatuma(nova_projekcija)
        if imaMesta == True:
            return nova_projekcija
        else:
            print("Zauzet termin za to vreme, probajte ponovo")


def izaberi_film():
    filmovi = uzmi_filmove()
    print_filmove()
    print("-" * 50)
    print("Izaberite jedan of filmova ili dodajte novi")
    print("-" * 50)
    while True:
        if try_str("Zelite li dodati novi film? Y or N: ").lower() == "y":
            novi_film = dodaj_film()
            return novi_film
        else:
            while True:
                print("-" * 50)
                idFilma = try_str("Unesite ID filma za projekciju: ")

                for film in filmovi:
                    if idFilma == film["ID"]:
                        return film


def dodaj_projekciju():
    projekcije = uzmi_projekcije()
    izabranFilm = izaberi_film()

    print("-" * 50)
    print("Projekcije koje vec postoje")
    prikazi_projekcije()

    while True:
        print("-" * 50)
        idProj = try_str("Unesite ID projekcije: ")
        postojiID = False

        for i in projekcije:
            if idProj == i["ID"]:
                print("Postoji ID, probajte ponovo")
                postojiID = True

        if postojiID == False:
            break

    if postojiID == False:
        nova_projekcija = prikupi_inpute(idProj, izabranFilm)
        print("Uspesno ste dodali projekciju")
        projekcije.append(nova_projekcija)
        zapisi_projekcije(projekcije)


def proveraDatuma(novaProjekcija):
    novaProjSat, novaProjMinut = novaProjekcija["Pocetak"].split("-")

    novaPocetak = datetime.timedelta(
        hours=int(novaProjSat), minutes=int(novaProjMinut))
    novaTrajanje = datetime.timedelta(minutes=int(novaProjekcija["Trajanje"]))

    novaKraj = novaPocetak + novaTrajanje
    novaSala = novaProjekcija["Sala"]

    projekcije = uzmi_projekcije()
    tajDatum = []
    for i in projekcije:
        if i["Datum"] == novaProjekcija["Datum"]:
            tajDatum.append(i)

    if len(tajDatum) == 0:
        imaMesta = True
        return imaMesta

    imaMesta = False
    for i in tajDatum:
        trajanjeProj = i["Trajanje"]
        pocetakProj = i["Pocetak"]

        sat, minut = pocetakProj.split("-")

        pocetak = datetime.timedelta(hours=int(sat), minutes=int(minut))
        trajanje = datetime.timedelta(minutes=int(trajanjeProj))

        kraj = pocetak + trajanje

        if novaKraj < pocetak:
            imaMesta = True
            break
        elif novaPocetak > kraj:

            imaMesta = True
        elif novaPocetak < kraj:
            if novaSala != i["Sala"]:
                imaMesta = True
                break
            else:
                imaMesta = False
                break
        else:
            if novaSala != i["Sala"]:
                imaMesta = True
                break
            else:
                print("else kraj")
                imaMesta = False

    return imaMesta


def izbrisi_projekciju():
    projekcije = uzmi_projekcije()

    prikazi_projekcije()

    nadjenaProjekcija = False

    while nadjenaProjekcija == False:
        print("-" * 50)
        id = try_int("Unesite ID projekcije za brisanje: ")

        for index, projekcija in enumerate(projekcije):
            if id == projekcija["ID"]:
                nadjenaProjekcija = True
                projekcije.pop(index)
                print("Uspesno ste izbrisali projekciju")

    zapisi_projekcije(projekcije)


def izmeni_projekciju():
    projekcije = uzmi_projekcije()

    print("-" * 50)
    print("Projekcije koje vec postoje")
    prikazi_projekcije()

    while True:
        print("-" * 50)
        idProj = try_str("Unesite ID projekcije: ")
        postoji = False

        for i in projekcije:
            if idProj == i["ID"]:
                izabrana_projekcija = i
                postoji = True

        if postoji == True:
            break

    print("-" * 50)
    print("Izabrali ste " + format_projekciju(izabrana_projekcija))
    print("-" * 50)
    print("Izaberite novi film za projekciju ")
    izabran_film = izaberi_film()
    print("-" * 50)
    print("Izabrali ste " + format_film(izabran_film))

    while True:
        Datum = try_datum("Unesite Datum projekcije, format - dd-m-yy: ")
        Pocetak = try_vreme("Unesite Pocetak projekcije, format - hh-mm: ")
        Cena = try_int("Unesite cenu Projekcije: ")
        Sala = izaberi_salu()

        izmenjena_projekcija = {
            "ID": izabrana_projekcija["ID"],
            "Naziv": izabran_film["Naziv"],
            "Zanr": izabran_film["Zanr"],
            "Cena": Cena,
            "Trajanje": izabran_film["Trajanje"],
            "Datum": Datum,
            "Pocetak": Pocetak,
            "Sala": Sala[0],
            "SlobodnoMesta": Sala[1],
            "UkupnoMesta": Sala[1]
        }

        imaMesta = proveraDatuma(izmenjena_projekcija)
        if imaMesta == True:
            for i, v in enumerate(projekcije):
                if izmenjena_projekcija["ID"] == v["ID"]:
                    projekcije[i] = izmenjena_projekcija
                    zapisi_projekcije(projekcije)
                    print("Uspesno ste izmenili projekciju")
                    return
        else:
            print("Zauzet termin, probajte ponovo")


def zapisi_projekcije(projekcije):
    kljucevi = uzmi_kljuceve_proj()
    kljucevi_string = ":".join(kljucevi)
    # kljucevi_string = "{}:{}:{}:{}:{}:{}:{}:{}:{}:{}".format(*kljucevi)

    projekcije_string = []
    for projekcija in projekcije:
        temp_str = "{ID}:{Naziv}:{Zanr}:{Cena}:{Trajanje}:{Datum}:{Pocetak}:{Sala}:{SlobodnoMesta}:{UkupnoMesta}".format(
            **projekcija)
        projekcije_string.append(temp_str)

    with open("data/projekcije.txt", "w") as f:
        f.writelines(kljucevi_string + "\n")
        for projekcija in projekcije_string:
            f.write(projekcija + "\n")
