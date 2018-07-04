from src import login
from src import menadzer


def start():
    korisnik = login.login()

    if korisnik["Uloga"] == "Menadzer":
        print("\n")
        print("Ulogovani kao Menadzer")
        menadzer.menadzer_meni()
    if korisnik["Uloga"] == "Prodavac":
        print("\n")
        print("Ulogovani kao Prodavac")
        prodavac_meni()


def prodavac_meni():
    print("Prodavac meni")


if __name__ == "__main__":
    start()
