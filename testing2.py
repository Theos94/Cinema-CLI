from testingErrors import try_int, try_str, try_funk

# Uzimamo filmove ovde, vraca filmove stavljene u array.
# TODO Skontati bolji nacin od temp_film dicta. Mora postojati


def uzmi_filmove():
    filmovi = []

    with open("filmoviTesting.txt", "r") as f:
        for line in f:
            line = line.strip()
            temp_film = line.split(":")
            temp_film = {
                "ID": temp_film[0],
                "Naziv": temp_film[1],
                "Zanr": temp_film[2],
                "Cena": temp_film[3],
                "Trajanje": temp_film[4]
            }

            filmovi.append(temp_film)
    return filmovi


def format_film(film):
    return "{Naziv} - {Zanr} - {Cena} - {Trajanje}".format(**film)


def print_filmove():
    filmovi = uzmi_filmove()

    for film in filmovi:
        print(format_film(film))
        print("-" * 50)


def zapisi_filmove(filmovi):
    filmovi_string = []
    for film in filmovi:
        temp_str = "{ID}:{Naziv}:{Zanr}:{Cena}:{Trajanje}".format(**film)
        filmovi_string.append(temp_str)

    with open("filmoviTesting.txt", "w") as f:
        for film in filmovi_string:
            f.write(film + "\n")


def dodaj_film():
    filmovi = uzmi_filmove()

    naziv = try_str("Naziv filma: ")
    zanr = try_str("Zanr: ")
    cena = try_str("Cena: ")
    trajanje = try_str("Trajanje: ")

    temp_film = {
        "ID": str(int(filmovi[-1]["ID"]) + 1),
        "Naziv": naziv,
        "Zanr": zanr,
        "Cena": cena,
        "Trajanje": trajanje
    }

    filmovi.append(temp_film)

    zapisi_filmove(filmovi)
