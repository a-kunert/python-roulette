from Mode import Mode

class NumberMode(Mode):
 
    
 
    def ask_for_bet(self):
        print("Welche Zahl zwischen 1 und 36 möchtest du spielen?")
        self.bet = int(input())

    def is_success(self,  result):
        return result["number"] == self.bet

    def get_factor(self):
        return 36
