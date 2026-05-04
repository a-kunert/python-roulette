from Mode import Mode

class RowMode(Mode):

    def ask_for_bet(self):
        print("Welche Zahlenreihe möchtest du wählen?")
        print("(1) für 1-18")
        print("(2) für 19-36")
        bet = int(input())
        self.bet = [[1, 18], [19, 36]][bet - 1]

    def get_factor(self):
        return 2

    def is_success(self, result):
        return self.bet[0] <= result["number"] <= self.bet[1]
