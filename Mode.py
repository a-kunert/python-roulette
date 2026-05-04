class Mode: 

    bet = 0

    def ask_for_bet(self):
        self.bet = 0

    def get_new_balance(self,balance,stake,bet,result):
        return balance-stake

    def get_factor(self):
        return 1

    def is_success(self,result):
        return False
    
    def print_result(self,result):
        print("")



