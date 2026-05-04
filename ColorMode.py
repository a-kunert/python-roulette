from Mode import Mode

class ColorMode(Mode):


    def ask_for_bet(self):
        print("Welche Farbe möchtest du spielen")
        print("(1) für Rot")
        print("(2) für Schwarz")
        bet = int(input())
        self.bet = ["red", "black"][bet - 1]

    def get_factor(self):
        return 2
    
    def is_success(self, result):
        return self.bet == result["color"]
    
    def print_result(self, result):
        return print(f"Farbe: {result['color']}")
    
