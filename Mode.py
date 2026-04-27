class Mode: 

    def ask_for_bet(self):
        return 0

    def get_new_balance(self,balance,stake,bet,result):
        return balance-stake

    def get_factor(self):
        return 1

    def is_success(self,bet,result):
        return False



