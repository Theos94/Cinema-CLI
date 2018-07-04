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