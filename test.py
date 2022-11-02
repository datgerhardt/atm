import unittest

from atm.atm import ATM


class TestATM(unittest.TestCase):
    def test_class_depense(self):
        atm = ATM([1, 2, 5], 111)
        self.assertEqual(atm.depense(), {
                         '1': 1, '5': 22},  "Should be {'1':1,'5':22}")

    def test_get_amt_by_denominations(self):
        atm = ATM([1, 2, 5])
        self.assertEqual(atm.get_amt_by_denominations({'1': 1, '5': 22, '50': 10}), {
                         '5': 122, '1': 1},  "Should be {'5': 122, '1': 1}")

    def test_bad_type(self):
        with self.assertRaises(TypeError):
            atm = ATM([1, '2', 5])

    # def test_denominations_with_zero(self):
    #     with self.assertRaises(ZeroDivisionError):
    #         atm = ATM([0])


if __name__ == "__main__":
    unittest.main()
