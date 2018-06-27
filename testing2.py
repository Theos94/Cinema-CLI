from testingErrors import try_int, try_str, try_funk

# TODO Skontati bolji nacin od temp_film dicta. Mora postojati
# Uzimamo filmove ovde, vraca filmove stavljene u array.


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

    filmovi = sortiraj_filmove(filmovi)
    return filmovi


def format_film(film):
    return "{ID} - {Naziv} - {Zanr} - {Cena} - {Trajanje}".format(**film)


def print_film(film):
    print("-" * 50)
    print(format_film(film))


def print_filmove():
    filmovi = uzmi_filmove()

    for film in filmovi:
        print("-" * 50)
        print(format_film(film))


def zapisi_filmove(filmovi):
    filmovi_string = []
    for film in filmovi:
        temp_str = "{ID}:{Naziv}:{Zanr}:{Cena}:{Trajanje}".format(**film)
        filmovi_string.append(temp_str)

    with open("filmoviTesting.txt", "w") as f:
        for film in filmovi_string:
            f.write(film + "\n")


def sortiraj_filmove(filmovi):
    sorted_filmovi = sorted(filmovi, key=lambda k: k["ID"])
    return sorted_filmovi


# TODO Dati korisniku opciju da ukuca ID! Ovako ce brljati program previse


def dodaj_film():
    filmovi = uzmi_filmove()

    naziv = try_str("Naziv filma: ")
    zanr = try_str("Zanr: ")
    cena = try_str("Cena: ")
    trajanje = try_str("Trajanje: ")

    temp_film = {
        "ID": str(len(filmovi) + 1),
        "Naziv": naziv,
        "Zanr": zanr,
        "Cena": cena,
        "Trajanje": trajanje
    }

    filmovi.append(temp_film)

    zapisi_filmove(filmovi)


def izbrisi_film():
    filmovi = uzmi_filmove()

    print_filmove()

    nadjenFilm = False

    while nadjenFilm == False:
        print("-" * 50)
        id = try_int("Unesite ID filma za brisanje: ")

        for index, film in enumerate(filmovi):
            if id == film["ID"]:
                nadjenFilm = True
                filmovi.pop(index)

    zapisi_filmove(filmovi)


def edit_film():
    filmovi = uzmi_filmove()

    print_filmove()

    def edit(index, film):
        print("-" * 50)
        naziv = try_str("Naziv filma: ")
        print("-" * 50)
        zanr = try_str("Zanr: ")
        print("-" * 50)
        cena = try_str("Cena: ")
        print("-" * 50)
        trajanje = try_str("Trajanje: ")
        print("-" * 50)

        filmovi[index] = {
            "ID": film["ID"],
            "Naziv": naziv,
            "Zanr": zanr,
            "Cena": cena,
            "Trajanje": trajanje
        }

        zapisi_filmove(filmovi)

    nadjenFilm = False

    while nadjenFilm == False:
        print("-" * 50)
        id = try_int("Unesite ID filma za editovanje: ")

        for index, film in enumerate(filmovi):
            if id == film["ID"]:
                nadjenFilm = True
                print_film(film)
                edit(index, film)
