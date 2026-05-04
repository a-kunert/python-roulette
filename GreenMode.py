from Mode import Mode

class GreenMode(Mode):
    def is_success(self, result):
        return result["number"] == 0

    def get_factor(self):
        return 36



