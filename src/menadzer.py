from errorHandler import try_int, try_str, try_funk
from projekcije import prikazi_projekcije, dodaj_projekciju, izbrisi_projekciju
from filmovi import print_filmove


def meni():
    print(50 * "-")
    print("Izaberite jednu od opcija ispod")
    print("1. Prikazi Filmove")
    print("2. Prikazi Projekcije")
    print("3. Dodaj Projekciju")
    print("4. Izmeni Projekciju")
    print("5. Izbrisi Projekciju")
    print("6. Dodaj Prodavca")
    print("7. Pretraga")
    print("8. Quit")
    print(50 * "-")


def navigacija(broj):
    if broj == "1":
        print("\n")
        print(50 * "-")
        print("Svi filmovi u databazi")
        print_filmove()
        menadzer_meni()
    elif broj == "2":
        print("\n")
        print(50 * "-")
        print("Sve projekcije u databazi")
        prikazi_projekcije()
        menadzer_meni()
    elif broj == "3":
        dodaj_projekciju()
        menadzer_meni()
    elif broj == "4":
        print("4")
    elif broj == "5":
        izbrisi_projekciju()
        menadzer_meni()
    elif broj == "6":
        print("6")
    elif broj == "7":
        print("7")
    elif broj == "8":
        quit()


def menadzer_meni():
    meni()
    navigacija(try_int("Unesite broj zeljene opcije: "))
