"""
Unit tests for the Hotel class.

This module contains tests that verify the functionality of the Hotel class,
ensuring that all methods behave as expected under various conditions.
"""

import unittest
import os
from hotel import Hotel
from room import Room


class TestHotel(unittest.TestCase):
    """Test cases for the Hotel class.

    This class implements unit tests for the Hotel class,
    room management, and information display functionalities.
    """
    def setUp(self):
        self.hotel = Hotel("Test Hotel", "Test loc")
        t_r = Room(rn=1, room_type="s", price=1.00, available=True)
        self.hotel.rs.append(t_r)

    def test_create_hotel(self):
        """Test creating a hotel correctly initializes its attributes."""
        name = "New hotel"
        loc = "New loc"
        hotel = Hotel.create_hotel(name, loc)
        self.assertEqual(hotel.name, name, "Name should match")
        self.assertEqual(hotel.loc, loc, "Loc should match")
        # Cleanup created hotel data file to avoid side effects
        os.remove(hotel.filename)

    def test_delete_hotel(self):
        """Test deleting a hotel removes its data file."""
        hotel = Hotel.create_hotel("Temporary Hotel", "Temporary loc")
        # Ensure the file exists before deletion
        self.assertTrue(os.path.exists(hotel.filename), "Data should exist")
        Hotel.delete_hotel(hotel)
        # Verify the file no longer exists
        self.assertFalse(os.path.exists(hotel.filename), "Data should delete")

    def test_display_information(self):
        """Test displaying hotel information"""
        expected_output = "Hotel Name: Test Hotel, loc: Test loc"
        self.assertEqual(self.hotel.display_information(), expected_output)

    def test_modify_information(self):
        """Test modifying hotel information updates the hotel attributes."""
        n_name = "Updated Test Hotel"
        n_loc = "Updated Test loc"
        self.hotel.modify_information(n_name=n_name, n_loc=n_loc)

        # Verify that the hotel's information has been updated
        self.assertEqual(self.hotel.name, n_name, "Name should be updated")
        self.assertEqual(self.hotel.loc, n_loc, "loc should be updated")

    def test_reserve_room(self):
        """Test reserving a room changes its availability."""

        rn = 1  # Define the room number as a variable

        # Attempt to reserve a room
        result = self.hotel.r_r("r_id", "c_id", rn, "2023-01-01", "2023-01-05")

        # Assert: Check the room is now reserved (not available)
        self.assertTrue(result, "Room reservation should succeed")
        reser_room = next((r for r in self.hotel.rs if r.rn == rn), None)
        self.assertIsNotNone(reser_room, "Reserved room should exist in hotel")
        self.assertFalse(reser_room.available, "Room should not available")

    def test_cancel_reservation(self):
        """Test canceling a reservation marks the room as available again."""
        # Setup: Create a hotel, add a room, and make a reservation
        hotel = Hotel("Hotel for Reservation", "Reservation loc")
        rn = 101
        hotel.rs.append(Room(rn, "double", 150))
        reser_id = "res101"
        hotel.r_r(reser_id, "cust101", rn, "2023-01-01", "2023-01-05")

        # Act: Cancel the reservation
        hotel.cancel_reservation(reser_id)

        # Assert: The room is available again
        room = next((room for room in hotel.rs if room.rn == rn), None)
        self.assertIsNotNone(room, "The room should exist.")
        self.assertTrue(room.available, "The room should be available")


if __name__ == '__main__':
    unittest.main()
