

def try_int(opis):
    while True:
        try:
            broj = input(opis)
            int(broj)
        except ValueError:
            print("Niste uneli broj, probajte ponovo")
        else:
            return broj


def try_str(opis):
    while True:
        try:
            str = input(opis)
            if not str:
                raise SyntaxError
        except SyntaxError:
            print("Niste uneli validan String")
        else:
            return str


def try_funk(funk, callback_funk):
    try:
        funk()
    except Exception as e:
        print(e)
        callback_funk()
        raise


