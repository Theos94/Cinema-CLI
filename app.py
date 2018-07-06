from src.login import login
from src.menadzer import menadzer_meni
from src.prodavac import prodavac_meni


def start():
    korisnik = login()

    if korisnik["Uloga"] == "Menadzer":
        print("\n")
        print("Ulogovani kao Menadzer")
        menadzer_meni()
    if korisnik["Uloga"] == "Prodavac":
        print("\n")
        print("Ulogovani kao Prodavac")
        prodavac_meni(korisnik)


if __name__ == "__main__":
    start()
