from src.login import login
from src.menadzer import menadzer_meni


def start():
    korisnik = login()

    if korisnik["Uloga"] == "Menadzer":
        print("\n")
        print("Ulogovani kao Menadzer")
        menadzer_meni()
    if korisnik["Uloga"] == "Prodavac":
        print("\n")
        print("Ulogovani kao Prodavac")
        prodavac_meni()


def prodavac_meni():
    print("Prodavac meni")


# if __name__ == "__main__":
#     start()

import sys

print(sys.path)