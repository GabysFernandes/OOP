
# Unit tests: python -m unittest -v
# Unit tests: python3 -m unittest -v
# Unit tests: py -m unittest -v

import unittest
from datetime import date, datetime

from event_countdown import EventCountdown
from time_and_date_driver import (
    days_until_next_birthday,
    days_until_next_christmas,
    next_birthday,
    parse_date,
)


class TestChristmasCountdown(unittest.TestCase):

    def test_christmas_day_has_zero_days_remaining(self) -> None:
        self.assertEqual(days_until_next_christmas(date(2026, 12, 25)), 0)

    def test_christmas_eve_has_one_day_remaining(self) -> None:
        self.assertEqual(days_until_next_christmas(date(2026, 12, 24)), 1)

    def test_after_christmas_uses_next_year(self) -> None:
        self.assertEqual(days_until_next_christmas(date(2026, 12, 26)), 364)


class TestBirthdayCountdown(unittest.TestCase):

    def test_birthday_is_today(self) -> None:
        self.assertEqual(days_until_next_birthday(6, 14, date(2026, 6, 14)), 0)

    def test_birthday_next_year(self) -> None:
        self.assertEqual(
            next_birthday(6, 14, date(2026, 6, 15)),
            date(2027, 6, 14)
        )

    def test_leap_day_birthday(self) -> None:
        self.assertEqual(
            next_birthday(2, 29, date(2026, 3, 1)),
            date(2028, 2, 29)
        )

    def test_invalid_month_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            days_until_next_birthday(13, 2, date(2026, 3, 1))


class TestEventCountdown(unittest.TestCase):

    def test_days_until_event(self) -> None:
        event = EventCountdown(date(2027, 1, 10), "Project deadline")
        self.assertEqual(event.get_days_remaining(date(2027, 1, 8)), 2)

    def test_past_event_is_negative(self) -> None:
        event = EventCountdown(date(2026, 1, 1))
        self.assertEqual(event.get_days_remaining(date(2026, 1, 3)), -2)

    def test_event_description_today(self) -> None:
        event = EventCountdown(date(2027, 1, 10), "Demo")
        self.assertEqual(event.describe(date(2027, 1, 10)), "Demo is today!")


class TestDateParsing(unittest.TestCase):

    def test_valid_date_string(self) -> None:
        self.assertEqual(
            parse_date("2026-12-31 23:59"),
            datetime(2026, 12, 31, 23, 59)
        )

    def test_invalid_date_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            parse_date("2026-15-40 23:59")


if __name__ == "__main__":
    unittest.main(verbosity=2)
