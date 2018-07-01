from login import login
from menadzer import menadzer_meni


def start():
    korisnik = login()

    if korisnik["Uloga"] == "Menadzer":
        print("\n")
        print("Ulogovani kao Menadzer")
        menadzer_meni()
    if korisnik["Uloga"] == "Prodavac":
        prodavac_meni()


def prodavac_meni():
    print("Prodavac meni")


if __name__ == "__main__":
    start()