from random import choice, randint
import csv

def bot_status_randomizer(fichero) -> str:
    listStatus = []
    with open(fichero, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for l in lector:
            status = str(l[0])
            listStatus.append(status)
    return choice(listStatus)

def get_random_color() -> int:
    return randint(0, 0xFFFFFF)

def esPar(numero: int) -> str:
    if numero % 2 == 0:
        res = "Es par"
    else:
        res = "Es impar"
    return res

def esPrimo(numero: int) -> str:
    if numero > 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                res = "No es primo"
                break
        else:
            res = "Es primo"
    else:
        res = "No es primo"
    return res