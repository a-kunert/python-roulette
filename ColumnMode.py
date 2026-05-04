from Mode import Mode

class ColumnMode(Mode):

    def ask_for_bet(self):
        print("Welche Kolonne möchtest du spielen? ")
        print("(1) für Längsreihe 1")
        print("(2) für Längsreihe 2")
        print("(3) für Längsreihe 3")
        self.bet = int(input())

    def get_factor(self):
        return 3

    def is_success(self, result):
        number = result["number"]
        if number == 0:
            return False
        return self.bet == number % 3

    def print_result(self,result):
        number = result["number"]
        if number == 0:
            return print("")
        if number % 3 == 0:
            return print("Reihe 3")
        return print(f"Reihe {number % 3}")








