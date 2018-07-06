from src.errorHandler import try_str


def uzmi_kljuceve_korisnika():
    kljucevi = []

    with open("data/korisnici.txt", "r") as f:
        kljucevi = f.readline().strip().split(":")

    return kljucevi


def uzmi_korisnike():
    korisnici = []

    with open("data/korisnici.txt", "r") as f:
        kljucevi = f.readline().strip().split(":")
        for line in f.readlines():
            korisnik = dict()
            for i, v in enumerate(line.strip().split(":")):
                korisnik[kljucevi[i]] = v
            korisnici.append(korisnik)
    return korisnici


def dodaj_prodavca():
    korisnici = uzmi_korisnike()

    username = try_str("Unesite korisnicko ime: ")
    lozinka = try_str("Unesite lozinku: ")
    lozinka2 = try_str("Ponovite lozinku: ")

    if lozinka != lozinka2:
        print("Lozinke se ne poklapaju")
        dodaj_prodavca()

    ime = try_str("Unesite ime korisnika: ")
    prezime = try_str("Unesite prezime korisnika: ")
    uloga = "Prodavac"

    novi_korisnik = {
        "Korisnicko": username,
        "Lozinka": lozinka,
        "Ime": ime,
        "Prezime": prezime,
        "Uloga": uloga
    }

    korisnici.append(novi_korisnik)
    zapisi_korisnike(korisnici)


def zapisi_korisnike(korisnici):
    kljucevi = uzmi_kljuceve_korisnika()
    kljucevi = ":".join(kljucevi)

    korisnici_string = []

    for korisnik in korisnici:
        temp_string = "{Korisnicko}:{Lozinka}:{Ime}:{Prezime}:{Uloga}".format(
            **korisnik)
        korisnici_string.append(temp_string)

    with open("data/korisnici.txt", "w") as f:
        f.writelines(kljucevi + "\n")
        for korisnik in korisnici_string:
            f.write(korisnik + "\n")