from Mode import Mode

class DozenMode(Mode):
    def ask_for_bet(self):
        print("Welches Dutzend möchtest du spielen")
        print("(1) für 1-12")
        print("(2) für 13-24")
        print("(3) für 25-36")
        bet = int(input())
        self.bet = [[1, 12], [13, 24], [25, 36]][bet - 1]

    def get_factor(self):
            return 3

    def is_success(self, result):
        number = result["number"]
        if number == 0:
            return False
        return (number - 1)//12 == self.bet

    def print_result(self,result):
        number = result["number"]
        if number == 0:
            return print("")
        return print(f"Dutzend {(number - 1)//12 +1}")



