from random import randint

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

saldo = 100

def game_saldo(current_saldo, stake, user_bet, result_number):
    print(result_number)
    if user_bet == result_number["color"]:
        if user_bet == "grün":
            return (current_saldo - stake) + (stake * 35)
        else:
            return (current_saldo - stake) + (stake * 2)
    else:
        return current_saldo - stake
    
# Modes:
# - Color
# - Number
# - Dozen
# - Parity
    
modes = ["Color","Number","Dozen","Parity"]    
mode = ""
    
while True:
    number = numbers[randint(0,36)]
    print("Welchen Modus möchtest du spielen")
    print("(1) für Farbe")
    print("(2) für Zahl")
    print("(3) für Dutzend")
    print("(4) für Parität")
    modeKey = int(input())
    mode = modes[modeKey -1]
    print(mode)
    money = int(input(f"Ihr Saldo beträgt {saldo}. Wie hoch ist ihr Einsatz?\n"))
    if saldo < money:
        print("Sie haben nicht genügend Saldo.")
        continue
    if money <= 0:
        print("Ungültiger Einsatz.")
        continue
    bet = input("Rot, schwarz oder grün? \n").lower()
    saldo = game_saldo(saldo, money, bet, number)
    print(f"Farbe: {number['color']}.")
    if bet == number['color']:
        print(f"Du hast die Runde gewonnen: Dein neues Saldo beträgt: {saldo}")
    else:
        print(f"Du hast leider verloren: Dein neues Saldo beträgt: {saldo}")
    if saldo == 0:
        print("Du bist pleite!")
        break


