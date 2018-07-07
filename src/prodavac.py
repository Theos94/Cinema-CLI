from src.errorHandler import try_int
from src.projekcije import prikazi_projekcije
from src.pretraga import pretraga
from src.karte import prodaj_karte


def meni():
    print(50 * "-")
    print("Izaberite jednu od opcija ispod")
    print("1. Prikazi Projekcije")
    print("2. Prodaj Karte")
    print("3. Pretraga")
    print("4. Quit")
    print(50 * "-")


def navigacija(korisnik):
    while True:
        broj = try_int("Unesite broj zeljene opcije: ")
        if broj == "1":
            print("\n")
            print(50 * "-")
            print("Sve projekcije u databazi")
            prikazi_projekcije()
            prodavac_meni(korisnik)
        elif broj == "2":
            prodaj_karte(korisnik)
            prodavac_meni(korisnik)
        elif broj == "3":
            pretraga()
            prodavac_meni(korisnik)
        elif broj == "4":
            quit()
        else:
            print("-" * 50)
            print("Niste uneli odgovarajuci broj, probajte ponovo")
            meni()


def prodavac_meni(korisnik):
    meni()
    navigacija(korisnik)