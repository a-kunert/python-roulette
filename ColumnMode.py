from Mode import Mode

class ColumnMode(Mode):

    def ask_for_bet(self):
        print("Welche Kolonne möchtest du spielen? ")
        print("(1) für Längsreihe 1")
        print("(2) für Längsreihe 2")
        print("(3) für Längsreihe 3")
        bet = int(input())
        self.bet = [
            [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],
            [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
            [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
        ][bet - 1]

    def get_factor(self):
        return 3

    def is_success(self, result):
        return result["number"] in self.bet
