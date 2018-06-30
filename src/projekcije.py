from errorHandler import try_int, try_str, try_funk
from filmovi import print_filmove, uzmi_filmove


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
    Sala = try_str("Unesite Salu projekcije: ")
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


def prikupi_inpute(idProj, izabranFilm):
    projekcije = uzmi_projekcije()

    while True:
        slobodanTermin = True

        Datum = try_str("Unesite Datum projekcije, format - dd-mm-yy: ")
        Pocetak = try_str("Unesite Pocetak projekcije, format - hh-mm: ")
        Sala = izaberi_salu()

        for i in projekcije:
            if Datum == i["Datum"] and Pocetak == i["Pocetak"] and Sala[0] == i["Sala"]:
                print("Zauzeta sala za taj termin, probajte ponovo!")
                slobodanTermin = False

        if slobodanTermin:
            break

    nova_projekcija = {
        "ID": idProj,
        "Naziv": izabranFilm["Naziv"],
        "Zanr": izabranFilm["Zanr"],
        "Cena": izabranFilm["Cena"],
        "Trajanje": izabranFilm["Trajanje"],
        "Datum": Datum,
        "Pocetak": Pocetak,
        "Sala": Sala[0],
        "SlobodnoMesta": Sala[1],
        "UkupnoMesta": Sala[1]
    }

    return nova_projekcija


def dodaj_projekciju():
    projekcije = uzmi_projekcije()
    filmovi = uzmi_filmove()

    print_filmove()

    while True:
        print("-" * 50)
        idFilma = try_str("Unesite ID filma za projekciju: ")
        postojiID = False

        for film in filmovi:
            if idFilma == film["ID"]:
                izabranFilm = film
                postojiID = True

        if postojiID == True:
            break

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

        projekcije.append(nova_projekcija)
        # zapisi_projekcije(projekcije)


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

    # zapisi_projekcije(projekcije)


def zapisi_projekcije(projekcije):
    kljucevi = uzmi_kljuceve_proj()

    kljucevi_string = "{}:{}:{}:{}:{}:{}:{}:{}:{}:{}".format(*kljucevi)

    projekcije_string = []
    for projekcija in projekcije:
        temp_str = "{ID}:{Naziv}:{Zanr}:{Cena}:{Trajanje}:{Datum}:{Pocetak}:{Sala}:{SlobodnoMesta}:{UkupnoMesta}".format(
            **projekcija)
        projekcije_string.append(temp_str)

    with open("data/projekcije.txt", "w") as f:
        f.writelines(kljucevi_string + "\n")
        for projekcija in projekcije_string:
            f.write(projekcija + "\n")