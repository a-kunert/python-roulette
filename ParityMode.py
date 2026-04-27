from Mode import Mode


class ParityMode(Mode):

    def ask_for_bet(self):
        print("Welche Parität möchtest du spielen")
        print("(1) für ungerade")
        print("(2) für gerade")
        bet = int(input())
        return bet


    def is_success(self, bet, result):
        return result["number"] != 0 and result["number"] % 2 == bet % 2

    def get_factor(self):
        return 2
