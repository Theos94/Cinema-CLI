from testingErrors import try_int, try_str, try_funk

# import datetime


def uzmi_kljuceve_proj():
    kljucevi = []

    with open("projekcije.txt", "r") as f:
        kljucevi = f.readline().strip().split(":")

    return kljucevi


def uzmi_filmove2():
    filmovi = []

    with open("filmoviTesting.txt", "r") as f:
        kljucevi = f.readline().strip().split(":")
        for line in f.readlines():
            film = dict()
            for i, v in enumerate(line.strip().split(":")):
                film[kljucevi[i]] = v
            filmovi.append(film)
    return filmovi


def uzmi_projekcije():
    projekcije = []

    with open("projekcije.txt", "r") as f:
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


def dodaj_projekciju():
    projekcije = uzmi_projekcije()
    filmovi = uzmi_filmove2()

    print(filmovi)

    idFilma = try_str("Unesite ID filma za projekciju: ")

    for film in filmovi:
        if idFilma == film["ID"]:
            izabranFilm = film

    idProj = try_str("Unesite ID projekcije: ")
    Datum = try_str("Unesite Datum projekcije, format - dd-mm-yy: ")
    Pocetak = try_str("Unesite Pocetak projekcije, format - hh-mm: ")
    Sala = try_str("Unesite Salu projekcije: ")
    SlobodnoMesta = try_str("Unesite SlobodnoMesta projekcije: ")
    UkupnoMesta = try_str("Unesite UkupnoMesta projekcije: ")

    nova_projekcija = {
        "ID": idProj,
        "Naziv": izabranFilm["Naziv"],
        "Zanr": izabranFilm["Zanr"],
        "Cena": izabranFilm["Cena"],
        "Trajanje": izabranFilm["Trajanje"],
        "Datum": Datum,
        "Pocetak": Pocetak,
        "Sala": Sala,
        "SlobodnoMesta": SlobodnoMesta,
        "UkupnoMesta": UkupnoMesta
    }

    projekcije.append(nova_projekcija)
    zapisi_projekcije(projekcije)


def zapisi_projekcije(projekcije):
    kljucevi = uzmi_kljuceve_proj()

    kljucevi_string = "{}:{}:{}:{}:{}:{}:{}:{}:{}:{}".format(*kljucevi)

    projekcije_string = []
    for projekcija in projekcije:
        temp_str = "{ID}:{Naziv}:{Zanr}:{Cena}:{Trajanje}:{Datum}:{Pocetak}:{Sala}:{SlobodnoMesta}:{UkupnoMesta}".format(
            **projekcija)
        projekcije_string.append(temp_str)

    with open("projekcije.txt", "w") as f:
        f.writelines(kljucevi_string + "\n")
        for projekcija in projekcije_string:
            f.write(projekcija + "\n")


dodaj_projekciju()

# ! Experiment sa datetime. Donekle radi, zahteva jos logike.
# ! Ipak odbaciti, previse vremena ce oduzeti
# trajanjeProj = uzmi_projekcije()[0]["Trajanje"]
# pocetakProj = uzmi_projekcije()[0]["Pocetak"]

# sat, minut = pocetakProj.split("-")

# pocetak = datetime.timedelta(hours=int(sat), minutes=int(minut))

# trajanje = datetime.timedelta(minutes=int(trajanjeProj))

# if ((pocetak + trajanje) < datetime.timedelta(hours=23, minutes=36)):
#     print("manje")
# else:
#     print("Vise")
