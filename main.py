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


def game_saldo(current_saldo, stake, user_bet, result_number, mode):
    if mode == "Color" and user_bet == result_number["color"]:
        return current_saldo + stake
    if mode == "Number" and user_bet == result_number["number"]:
        return current_saldo + stake * 35
    if mode == "Dozen" and user_bet[0] <= result_number["number"] <= user_bet[1]:
        return current_saldo + stake * 2
    if mode == "Parity" and result_number["number"] % 2 == user_bet % 2:
        return current_saldo + stake
    if mode == "Green" and result_number["number"] == 0:
        return current_saldo + stake * 35
    return current_saldo - stake


modes = ["Color", "Number", "Dozen", "Parity", "Green"]

while True:
    number = numbers[randint(0, 36)]
    print("Welchen Modus möchtest du spielen")
    print("(1) für Farbe")
    print("(2) für Zahl")
    print("(3) für Dutzend")
    print("(4) für Parität")
    print("(5) für Grün")
    modeKey = int(input())
    mode = modes[modeKey - 1]
    print(mode)
    money = int(input(f"Ihr Saldo beträgt {saldo}. Wie hoch ist ihr Einsatz?\n"))
    if saldo < money:
        print("Sie haben nicht genügend Saldo.")
        continue
    if money <= 0:
        print("Ungültiger Einsatz.")
        continue

    bet = 0
    if mode == "Color":
        print("Welche Farbe möchtest du spielen")
        print("(1) für Rot")
        print("(2) für Schwarz")
        bet = int(input())
        bet = ["red", "black"][bet - 1]
    if mode == "Number":
        print("Welche Zahl zwischen 1 und 36 möchtest du spielen?")
        bet = int(input())
    if mode == "Dozen":
        print("Welches Dutzend möchtest du spielen")
        print("(1) für 1-12")
        print("(2) für 13-24")
        print("(3) für 25-36")
        bet = int(input())
        bet = [[1, 12], [13, 24], [25, 36]][bet - 1]
    if mode == "Parity":
        print("Welche Parität möchtest du spielen")
        print("(1) für ungerade")
        print("(2) für gerade")
        bet = int(input())

    oldSaldo = saldo
    saldo = game_saldo(saldo, money, bet, number, mode)
    print(f"Zahl: {number['number']}, Farbe: {number['color']}.")

    if saldo > oldSaldo:
        print(f"Du hast die Runde gewonnen: Dein neues Saldo beträgt: {saldo}")
    else:
        print(f"Du hast leider verloren: Dein neues Saldo beträgt: {saldo}")
    if saldo == 0:
        print("Du bist pleite!")
        break
