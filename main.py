from random import randint

from ColorMode import ColorMode
from DozenMode import DozenMode
from GreenMode import GreenMode
from NumberMode import NumberMode
from ParityMode import ParityMode
from ColumnMode import ColumnMode
from RowMode import RowMode

numbers = [
    {"number": 0, "color": "green"},
    {"number": 1, "color": "red"},
    {"number": 2, "color": "black"},
    {"number": 3, "color": "red"},
    {"number": 4, "color": "black"},
    {"number": 5, "color": "red"},
    {"number": 6, "color": "black"},
    {"number": 7, "color": "red"},
    {"number": 8, "color": "black"},
    {"number": 9, "color": "red"},
    {"number": 10, "color": "black"},
    {"number": 11, "color": "black"},
    {"number": 12, "color": "red"},
    {"number": 13, "color": "black"},
    {"number": 14, "color": "red"},
    {"number": 15, "color": "black"},
    {"number": 16, "color": "red"},
    {"number": 17, "color": "black"},
    {"number": 18, "color": "red"},
    {"number": 19, "color": "red"},
    {"number": 20, "color": "black"},
    {"number": 21, "color": "red"},
    {"number": 22, "color": "black"},
    {"number": 23, "color": "red"},
    {"number": 24, "color": "black"},
    {"number": 25, "color": "red"},
    {"number": 26, "color": "black"},
    {"number": 27, "color": "red"},
    {"number": 28, "color": "black"},
    {"number": 29, "color": "black"},
    {"number": 30, "color": "red"},
    {"number": 31, "color": "black"},
    {"number": 32, "color": "red"},
    {"number": 33, "color": "black"},
    {"number": 34, "color": "red"},
    {"number": 35, "color": "black"},
    {"number": 36, "color": "red"}
]

balance = 100


modes = [
    ColorMode(),
    NumberMode(),
    DozenMode(),
    ParityMode(),
    GreenMode(),
    ColumnMode(),
    RowMode(),
]


while True:
    number = numbers[randint(0, 36)]
    print("Welchen Modus möchtest du spielen")
    print("(1) für Farbe")
    print("(2) für Zahl")
    print("(3) für Dutzend")
    print("(4) für Parität")
    print("(5) für Grün")
    print("(6) für Kolonne")
    print("(7) für Zahlenreihe")
    modeKey = int(input())
    mode = modes[modeKey - 1]
    
    bet = mode.ask_for_bet()
    
    stake = int(input(f"Ihr Saldo beträgt {balance}. Wie hoch ist ihr Einsatz?\n"))
    if balance < stake:
        print("Sie haben nicht genügend Saldo.")
        continue
    if stake <= 0:
        print("Ungültiger Einsatz.")
        continue

    balance -= stake
    if mode.is_success(bet,number):
        balance += stake * mode.get_factor()
    print(f"Zahl: {number['number']}, Farbe: {number['color']}.")

    if mode.is_success(bet,number):
        print(f"Du hast die Runde gewonnen: Dein neues Saldo beträgt: {balance}")
    else:
        print(f"Du hast leider verloren: Dein neues Saldo beträgt: {balance}")
    if balance == 0:
        print("Du bist pleite!")
        break
