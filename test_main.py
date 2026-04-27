import pytest
from main import game_saldo, numbers


class TestGameSaldo:
    """Tests for the game_saldo function"""

    def test_win_on_red(self):
        """Test winning when betting on red"""
        current_saldo = 100
        stake = 10
        user_bet = "red"
        result_number = {"number": 1, "color": "red"}

        new_saldo = game_saldo(current_saldo, stake, user_bet, result_number)
        assert new_saldo == 110  # 100 - 10 + (10 * 2)

    def test_win_on_black(self):
        """Test winning when betting on black"""
        current_saldo = 100
        stake = 20
        user_bet = "black"
        result_number = {"number": 2, "color": "black"}

        new_saldo = game_saldo(current_saldo, stake, user_bet, result_number)
        assert new_saldo == 120  # 100 - 20 + (20 * 2)

    def test_win_on_green(self):
        """Test winning when betting on green (0)"""
        current_saldo = 100
        stake = 10
        user_bet = "green"
        result_number = {"number": 0, "color": "green"}

        new_saldo = game_saldo(current_saldo, stake, user_bet, result_number)
        assert new_saldo == 440  # 100 - 10 + (10 * 35)

    def test_lose_on_red_when_black_comes(self):
        """Test losing when betting on red but black comes up"""
        current_saldo = 100
        stake = 10
        user_bet = "red"
        result_number = {"number": 2, "color": "black"}

        new_saldo = game_saldo(current_saldo, stake, user_bet, result_number)
        assert new_saldo == 90  # 100 - 10

    def test_lose_on_black_when_red_comes(self):
        """Test losing when betting on black but red comes up"""
        current_saldo = 100
        stake = 15
        user_bet = "black"
        result_number = {"number": 1, "color": "red"}

        new_saldo = game_saldo(current_saldo, stake, user_bet, result_number)
        assert new_saldo == 85  # 100 - 15

    def test_lose_on_green_when_red_comes(self):
        """Test losing when betting on green but red comes up"""
        current_saldo = 100
        stake = 10
        user_bet = "green"
        result_number = {"number": 1, "color": "red"}

        new_saldo = game_saldo(current_saldo, stake, user_bet, result_number)
        assert new_saldo == 90  # 100 - 10

    def test_multiple_rounds_winning(self):
        """Test multiple consecutive wins"""
        saldo = 100
        stake = 10

        # First win on red
        result = {"number": 1, "color": "red"}
        saldo = game_saldo(saldo, stake, "red", result)
        assert saldo == 110

        # Second win on black
        result = {"number": 2, "color": "black"}
        saldo = game_saldo(saldo, stake, "black", result)
        assert saldo == 120

    def test_multiple_rounds_losing(self):
        """Test multiple consecutive losses"""
        saldo = 100
        stake = 10

        # First loss
        result = {"number": 1, "color": "red"}
        saldo = game_saldo(saldo, stake, "black", result)
        assert saldo == 90

        # Second loss
        result = {"number": 2, "color": "black"}
        saldo = game_saldo(saldo, stake, "red", result)
        assert saldo == 80

    def test_high_stake_win(self):
        """Test winning with a high stake"""
        current_saldo = 1000
        stake = 500
        user_bet = "red"
        result_number = {"number": 1, "color": "red"}

        new_saldo = game_saldo(current_saldo, stake, user_bet, result_number)
        assert new_saldo == 1500  # 1000 - 500 + (500 * 2)

    def test_high_stake_loss(self):
        """Test losing with a high stake"""
        current_saldo = 1000
        stake = 500
        user_bet = "red"
        result_number = {"number": 2, "color": "black"}

        new_saldo = game_saldo(current_saldo, stake, user_bet, result_number)
        assert new_saldo == 500  # 1000 - 500

    def test_saldo_reaches_zero(self):
        """Test when saldo reaches exactly zero after a loss"""
        current_saldo = 10
        stake = 10
        user_bet = "red"
        result_number = {"number": 2, "color": "black"}

        new_saldo = game_saldo(current_saldo, stake, user_bet, result_number)
        assert new_saldo == 0


class TestNumbersList:
    """Tests for the numbers list structure"""

    def test_numbers_list_length(self):
        """Test that we have all 37 numbers (0-36)"""
        assert len(numbers) == 37

    def test_all_numbers_present(self):
        """Test that all numbers from 0 to 36 are present"""
        number_values = [num["number"] for num in numbers]
        assert sorted(number_values) == list(range(37))

    def test_zero_is_green(self):
        """Test that 0 is green"""
        zero = next(num for num in numbers if num["number"] == 0)
        assert zero["color"] == "green"

    def test_red_numbers_count(self):
        """Test that we have 18 red numbers"""
        red_count = sum(1 for num in numbers if num["color"] == "red")
        assert red_count == 18

    def test_black_numbers_count(self):
        """Test that we have 18 black numbers"""
        black_count = sum(1 for num in numbers if num["color"] == "black")
        assert black_count == 18

    def test_green_numbers_count(self):
        """Test that we have only 1 green number"""
        green_count = sum(1 for num in numbers if num["color"] == "green")
        assert green_count == 1

    def test_correct_red_numbers(self):
        """Test that the correct numbers are red"""
        expected_red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        actual_red = sorted([num["number"] for num in numbers if num["color"] == "red"])
        assert actual_red == expected_red


class TestRandomGameOutcomes:
    """Tests that verify game outcomes with random number selection"""

    def test_random_spin_betting_on_color(self):
        """Test a game round with random number - verify either win or loss occurs"""
        from random import randint

        current_saldo = 100
        stake = 10
        user_bet = "red"

        # Get a random number from the wheel
        random_number = numbers[randint(0, 36)]
        new_saldo = game_saldo(current_saldo, stake, user_bet, random_number)

        # Check that saldo is either win (110) or loss (90)
        if random_number["color"] == "red":
            assert new_saldo == 110, f"Expected win: 110, got {new_saldo}"
        else:
            assert new_saldo == 90, f"Expected loss: 90, got {new_saldo}"

    def test_random_spin_betting_on_green(self):
        """Test betting on green with random number"""
        from random import randint

        current_saldo = 100
        stake = 10
        user_bet = "green"

        random_number = numbers[randint(0, 36)]
        new_saldo = game_saldo(current_saldo, stake, user_bet, random_number)

        # Check that saldo is either big win (440) or loss (90)
        if random_number["color"] == "green":
            assert new_saldo == 440, f"Expected green win: 440, got {new_saldo}"
        else:
            assert new_saldo == 90, f"Expected loss: 90, got {new_saldo}"

    def test_multiple_random_spins(self):
        """Test 10 random spins and verify saldo changes are correct"""
        from random import randint

        saldo = 1000
        stake = 10

        for _ in range(10):
            previous_saldo = saldo
            random_number = numbers[randint(0, 36)]
            user_bet = "red"  # Always bet on red

            saldo = game_saldo(saldo, stake, user_bet, random_number)

            # Verify the change is correct
            if random_number["color"] == "red":
                assert saldo == previous_saldo + stake, "Win calculation incorrect"
            else:
                assert saldo == previous_saldo - stake, "Loss calculation incorrect"
