"""
Unit tests for the Reservation class.

This module contains tests to verify the functionality of the Reservation class
ensuring that all methods behave as expected under various conditions.
"""

import unittest
import os
from reservation import Reservation, make_reservation


class TestReservation(unittest.TestCase):
    """Tests for functionality of the Reservation class."""
    def setUp(self):
        """Setup method to create a reservation instance before each test."""
        self.reservation_data = {
            'reser_id': 1,
            'customer_id': 1,
            'hotel_name': 'Hotel A',
            'room_number': 1,
            'start_date': '2023-01-01',
            'end_date': '2023-01-05'
        }
        self.reservation = make_reservation(**self.reservation_data)

    def test_reservation_initialization(self):
        """Test the initialization of a reservation."""
        for key, value in self.reservation_data.items():
            self.assertEqual(getattr(self.reservation, key), value)

    def test_save_to_file(self):
        """Test saving a reservation details to a file."""
        self.reservation.save_to_file()
        expected_filename = f"reservation_{self.reservation.reser_id}.json"
        self.assertTrue(os.path.exists(expected_filename))
        # Clean up
        os.remove(expected_filename)

    def test_cancel_reservation(self):
        """Test canceling a reservation by removing its file."""
        self.reservation.save_to_file()
        Reservation.cancel_reservation(self.reservation.reser_id)
        expected_filename = f"reservation_{self.reservation.reser_id}.json"
        self.assertFalse(os.path.exists(expected_filename))

    # Add more tests as necessary for other methods and edge cases.


if __name__ == '__main__':
    unittest.main()
