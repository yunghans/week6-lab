import unittest

from duckfine import DuckFine


class TestDuckFine(unittest.TestCase):
    def test_initializes_member_id_and_zero_balance(self):
        fine = DuckFine("member-123")

        self.assertEqual(fine.member_id, "member-123")
        self.assertEqual(fine.total_owed, 0.0)

    def test_forgives_first_two_days_late(self):
        fine = DuckFine("member-123")

        self.assertEqual(fine.charge(2), 0.0)

    def test_charges_daily_fee_after_grace_period(self):
        fine = DuckFine("member-123")

        self.assertEqual(fine.charge(5), 1.50)

    def test_deluxe_ducks_double_the_fee(self):
        fine = DuckFine("member-123")

        self.assertEqual(fine.charge(5, deluxe=True), 3.00)

    def test_single_charge_does_not_exceed_maximum_fee(self):
        fine = DuckFine("member-123")

        self.assertEqual(fine.charge(20), 5.00)

    def test_charges_are_added_to_total_owed(self):
        fine = DuckFine("member-123")

        fine.charge(3)
        fine.charge(4)

        self.assertEqual(fine.total_owed, 1.50)

    def test_rejects_negative_days_late(self):
        fine = DuckFine("member-123")

        with self.assertRaises(ValueError):
            fine.charge(-1)


if __name__ == "__main__":
    unittest.main()