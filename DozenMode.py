from Mode import Mode

class DozenMode(Mode):
    def ask_for_bet(self):
        print("Welches Dutzend möchtest du spielen")
        print("(1) für 1-12")
        print("(2) für 13-24")
        print("(3) für 25-36")
        bet = int(input())
        return [[1, 12], [13, 24], [25, 36]][bet - 1]


    def get_factor(self):
            return 3

    def is_success(self, bet, result):
        return bet[0] <= result["number"] <= bet[1]



