from src.errorHandler import try_int, try_str, try_datum, try_vreme, try_minutes
import datetime


def uzmi_kljuceve_filmova():
    kljucevi = []

    with open("data/filmovi.txt", "r") as f:
        kljucevi = f.readline().strip().split(":")

    return kljucevi


def uzmi_filmove():
    filmovi = []

    with open("data/filmovi.txt", "r") as f:
        kljucevi = f.readline().strip().split(":")
        for line in f.readlines():
            film = dict()
            for i, v in enumerate(line.strip().split(":")):
                film[kljucevi[i]] = v
            filmovi.append(film)
    filmovi = sortiraj_filmove(filmovi)
    return filmovi


def format_film(film):
    return "{ID} - {Naziv} - {Zanr} - {Trajanje}".format(**film)


def print_film(film):
    print("-" * 50)
    print(format_film(film))


def print_filmove():
    filmovi = uzmi_filmove()

    for film in filmovi:
        print("-" * 50)
        print(format_film(film))


def sortiraj_filmove(filmovi):
    sorted_filmovi = sorted(filmovi, key=lambda k: k["ID"])
    return sorted_filmovi


def dodaj_film():
    filmovi = uzmi_filmove()

    naziv = try_str("Naziv filma: ")
    zanr = try_str("Zanr: ")
    trajanje = try_minutes("Trajanje u minutima: ")

    temp_film = {
        "ID": str(len(filmovi) + 1),
        "Naziv": naziv,
        "Zanr": zanr,
        "Trajanje": trajanje
    }

    filmovi.append(temp_film)
    zapisi_filmove(filmovi)
    return (temp_film)


def zapisi_filmove(filmovi):
    kljucevi = uzmi_kljuceve_filmova()
    kljucevi_string = ":".join(kljucevi)

    filmovi_string = []
    for film in filmovi:
        temp_str = "{ID}:{Naziv}:{Zanr}:{Trajanje}".format(**film)
        filmovi_string.append(temp_str)

    with open("data/filmovi.txt", "w") as f:
        f.writelines(kljucevi_string + "\n")
        for film in filmovi_string:
            f.write(film + "\n")
