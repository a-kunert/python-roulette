from Mode import Mode

class NumberMode(Mode):
 
    def ask_for_bet(self):
        print("Welche Zahl zwischen 1 und 36 möchtest du spielen?")
        bet = int(input())
        return bet

    def is_success(self, bet, result):
        return result["number"] == bet

    def get_factor(self):
        return 36