from src.errorHandler import try_int
from src.projekcije import uzmi_projekcije, format_projekciju, zapisi_projekcije, prikazi_projekcije
import datetime
import uuid


def izaberi_projekciju(projekcije):
    while True:
        print("-" * 50)
        unosID = try_int("Unesite ID projekcije: ")

        for i in projekcije:
            if unosID.strip() == i["ID"]:
                izabranaProjekcija = i
                return izabranaProjekcija
        print("Ne postoji taj ID, probajte ponovo")
        print("-" * 50)


def prodaj_karte(prodavac):
    projekcije = uzmi_projekcije()

    prikazi_projekcije()

    izabranaProjekcija = izaberi_projekciju(projekcije)

    print("-" * 50)
    print("Izabrali ste --- " + format_projekciju(izabranaProjekcija))
    print("-" * 50)
    brojKarata = try_int("Unesite broj karata za prodati: ")

    if int(brojKarata) > int(izabranaProjekcija["SlobodnoMesta"]):
        print("Nedovoljno slobodnih mesta")
        return
    else:
        racun = int(brojKarata) * int(izabranaProjekcija["Cena"])

    izabranaProjekcija["SlobodnoMesta"] = str(
        int(izabranaProjekcija["SlobodnoMesta"]) - int(brojKarata))

    for i in projekcije:
        if izabranaProjekcija["ID"] == i["ID"]:
            i = izabranaProjekcija

    print("\n")
    print("-" * 50)
    print("Uspesno prodato {} karata za {} ".format(
        str(brojKarata), izabranaProjekcija["Naziv"]))
    print("-" * 50)
    print("Ukupno za platiti: " + str(racun) + "rsd")
    print("-" * 50)

    zapisi_projekcije(projekcije)
    zapisi_racun(racun, izabranaProjekcija, projekcije, prodavac, brojKarata)


def zapisi_racun(racun, izabranaProjekcija, projekcije, prodavac, brojKarata):
    datum = datetime.datetime.now()
    racun = """
--------------------------
        Racun
Projekcija: {}
    -Datum: {}
    -Pocetak: {}
    -Sala: {}
Broj karata: {}
Iznos: {} rsd
Prodavac: {} {}
Datum: {}
Sifra racuna: {}
--------------------------
""".format(izabranaProjekcija["Naziv"], izabranaProjekcija["Datum"],
           izabranaProjekcija["Pocetak"], izabranaProjekcija["Sala"],
           brojKarata, racun, prodavac["Ime"], prodavac["Prezime"],
           datum.strftime("%d/%m/%y - %H-%M"),
           str(uuid.uuid1())[:8])

    print(racun)

    with open("data/racuni.txt", "a") as f:
        f.write(racun + "\n")