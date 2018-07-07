from src.errorHandler import try_int, try_str
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


def uzmi_karte(projekcije):

    for i in projekcije:
        print("-" * 100)
        print(format_projekciju(i))

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

    racun_dict = {
        "racun": racun,
        "izabranaProjekcija": izabranaProjekcija,
        "projekcije": projekcije,
        "brojKarata": brojKarata
    }

    return racun_dict


def prodaj_karte(prodavac):
    projekcije = uzmi_projekcije()
    racuni = []
    print("-" * 50)
    print("Prodaja Karata")
    print("-" * 50)
    racun_dict = uzmi_karte(projekcije)
    racuni.append(racun_dict)
    print("-" * 50)

    while True:
        print("-" * 50)
        pitanje = try_str(
            "Zelite li dodati jos projekcija na racun ili ne? Odg sa Y or N: ")
        if pitanje.lower() == "y":
            racun_dict = uzmi_karte(racun_dict["projekcije"])
            racuni.append(racun_dict)
            for i in racuni:
                i["projekcije"] = racun_dict["projekcije"]
        else:
            print("-" * 50)
            print("Zavrseno dodavanje karata")
            zapisi_racun(racuni, prodavac)
            break


def zapisi_racun(racuni, prodavac):
    print("-" * 50)
    odgovor = try_str("Zelite li izdati racun? Odg sa Y or N: ")
    if odgovor.lower() == "y":
        print("-" * 50)
        datum = datetime.datetime.now()
        zapisi_projekcije(racuni[-1]["projekcije"])

        ukupnoPlatiti = 0

        izabraneProjekcije = []

        for i in racuni:
            ukupnoPlatiti += int(i["racun"])
            temp_dict = {
                "izabranaProjekcija": i["izabranaProjekcija"],
                "brojKarata": i["brojKarata"]
            }

            izabraneProjekcije.append(temp_dict)

        racuni = []
        racuni.append("\n  Racun - " + str(uuid.uuid1())[:8])
        for i in izabraneProjekcije:
            racun = """--------------------------
Projekcija: {}
    -Datum: {}
    -Pocetak: {}
    -Sala: {}
    Broj karata: {}
--------------------------""".format(i["izabranaProjekcija"]["Naziv"],
                                     i["izabranaProjekcija"]["Datum"],
                                     i["izabranaProjekcija"]["Pocetak"],
                                     i["izabranaProjekcija"]["Sala"],
                                     i["brojKarata"])
            racuni.append(racun)
        opis_racuna = """
Ukupan Iznos: {} rsd
Prodavac: {} {}
Datum Izdavanja: {}
Sifra racuna: {}
--------------------------""".format(ukupnoPlatiti, prodavac["Ime"],
                                     prodavac["Prezime"],
                                     datum.strftime("%d/%m/%y - %H-%M"),
                                     str(uuid.uuid1())[:8])
        racuni.append(opis_racuna)

        for i in racuni:
            print(i)
            with open("data/racuni.txt", "a") as f:
                f.write(i + "\n")
