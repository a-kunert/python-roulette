from Mode import Mode

class ColorMode(Mode):


    def ask_for_bet(self):
        print("Welche Farbe möchtest du spielen")
        print("(1) für Rot")
        print("(2) für Schwarz")
        bet = int(input())
        bet = ["red", "black"][bet - 1]
        return bet

    def get_factor(self):
        return 2
    
    def is_success(self, bet, result):
        return bet == result["color"]

