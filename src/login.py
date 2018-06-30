from errorHandler import try_int, try_str, try_funk


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


def login():
    korisnici = uzmi_korisnike()
    print(50 * "-")
    print("Dobrodosli u Cinema CLI.")
    print(50 * "-")

    while True:
        username = try_str("Unesite vase Korisnicko Ime: ")
        print(50 * "-")
        lozinka = try_str("Unesite vasu Lozinku: ")

        for korisnik in korisnici:
            if korisnik["Korisnicko"].lower() == username.lower(
            ) and korisnik["Lozinka"] == lozinka:
                return korisnik
        else:
            print(50 * "-")
            print("Pogresni podaci, probajte ponovo")
            print(50 * "-")
