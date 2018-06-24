import json
from testingErrors import try_int, try_str, try_funk

# Ispod stari nacini za otvaranje filmova, posto moze da se koristi JSON za podatke dole sa njim radim

# with open("filmovi.txt") as f:
#     content = f.readlines()
#     print(content)
#
# lines = [line.rstrip('\n') for line in open("filmovi.txt")]

# with open("filmoviBackup.txt", "r") as f:
#     read_data = f.read()
#
#
# x = json.loads(read_data)



# with open("filmovi.txt", "r") as filmovi:
#     for line in filmovi:
#         film = line.split(",")
#         naziv = film[1]
#         realNaziv = naziv.split(":")[1][2:-1]
#         print(realNaziv)

def format_film(film):
    return "{naziv} - {zanr} - {trajanje}".format(**film)

def print_filmove():
    with open("filmoviBackup.txt", "r") as f:
        data = f.read()

    filmovi = json.loads(data)

    for film in filmovi:
        print(format_film(film))


print_filmove()

def dodaj_film():

    with open("filmoviBackup.txt", "r") as f:
        data = f.read()


    filmovi = json.loads(data)


    naziv = try_str("Naziv filma: ")
    zanr = try_str("Zanr: ")
    trajanje = try_str("Trajanje: ")



    # temp_dict = {
    #     "ID": str(len(filmovi) + 1),
    #     "naziv": naziv,
    #     "zanr": zanr,
    #     "trajanje": trajanje
    # }


    temp_dict = {
        "ID": str(int(filmovi[-1]["ID"]) + 1),
        "naziv": naziv,
        "zanr": zanr,
        "trajanje": trajanje
    }



    filmovi.append(temp_dict)
    with open("filmoviBackup.txt", "w") as f:
        f.write(json.dumps(filmovi))

def main_menu():
    print("1. MENIIIII")
    izbor = input("Dodajte film - 1.")
    if izbor == "1":
        try_funk(dodaj_film, main_menu)
    else:
        print("GOODBYEEEE")



def izmeni_film():
    with open("filmoviBackup.txt", "r") as f:
        data = f.read()


    filmovi = json.loads(data)

    id = try_int("Unesite ID filma za izmenu: ")

    for index, film in enumerate(filmovi):
        if id == film["ID"]:
            print(film, index)
            nov_naziv = try_str("Unesite novi naziv Filma: ")
            nov_zanr = try_str("Unesite novi zanr Filma: ")
            nov_trajanje = try_str("Unesite novo trajanje Filma: ")
            filmovi[index] = {
                "ID": id,
                "naziv": nov_naziv,
                "zanr": nov_zanr,
                "trajanje": nov_trajanje
            }

            with open("filmoviBackup.txt", "w") as f:
                f.write(json.dumps(filmovi))




def izbrisi_film():
    with open("filmoviBackup.txt", "r") as f:
        data = f.read()


    filmovi = json.loads(data)

    id = try_int("Unesite ID filma za brisanje: ")

    for index, film in enumerate(filmovi):
        if id == film["ID"]:
            filmovi.pop(index)
            with open("filmoviBackup.txt", "w") as f:
                f.write(json.dumps(filmovi))


# try_funk(izmeni_film, main_menu)
# try_funk(izbrisi_film, main_menu)
# try_funk(dodaj_film, main_menu)