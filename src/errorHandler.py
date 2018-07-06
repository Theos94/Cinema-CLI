import datetime


def try_int(opis):
    while True:
        try:
            broj = input(opis)
            int(broj)

        except ValueError:
            print("Niste uneli broj, probajte ponovo")
        else:
            return broj.strip()


def try_str(opis):
    while True:
        try:
            string = input(opis)
            if not str:
                raise SyntaxError
            if len(string) > 20 or string.strip() == "":
                raise SyntaxError
        except SyntaxError:
            print("Niste uneli validan String")
        else:
            return string.strip()


def try_funk(funk, callback_funk):
    try:
        funk()
    except Exception as e:
        print(e)
        callback_funk()
        raise


def try_datum(opis):
    while True:
        try:
            datum = input(opis)
            datetime.datetime.strptime(datum, '%d-%m-%Y')
        except ValueError:
            print("Niste uneli validan Datum")
        else:
            return datum.strip()


def try_datum_bez(datum):
    try:
        if datetime.datetime.strptime(datum, "%d"):
            return datum
    except ValueError:
        return datum


def try_vreme(opis):
    while True:
        try:
            vreme = input(opis)
            datetime.datetime.strptime(vreme, "%H-%M")
        except ValueError:
            print("Niste uneli validno Vreme")
        else:
            return vreme.strip()


def try_minutes(opis):
    while True:
        try:
            minuti = input(opis)
            int(minuti)
            datetime.timedelta(minutes=int(minuti))
            if int(minuti) > 260:
                raise ValueError
        except ValueError:
            print("Pogresno uneti minuti")
        else:
            return minuti.strip()
