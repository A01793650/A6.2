"""
Module for managing hotel data in the reservation system.

Author: Jessica Pulido
Last edited: February 18, 2024
"""

import json
import os
from reservation import make_reservation
from room import Room


class Hotel:
    """Represents a hotel within the reservation system, with persistence."""

    def __init__(self, name, loc):
        """Initializes a Hotel object with a name and loc."""
        self.name = name
        self.loc = loc
        self.rs = []  # Could be a list of Room objects
        self.filename = f"{name}_data.json"

    def save_to_file(self):
        """Saves hotel data to a file."""
        data = {
            'name': self.name,
            'loc': self.loc,
            'rs': [room.to_dict() for room in self.rs]
        }
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    def load_from_file(self):
        """Loads hotel data from a file."""
        with open(self.filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.name = data['name']
        self.loc = data['loc']
        # Assume a from_dict class method for Room to reconstruct room objects
        self.rs = [Room.from_dict(room_data) for room_data in data['rs']]

    @staticmethod
    def create_hotel(name, loc):
        """Creates a new hotel and saves it to a file."""
        hotel = Hotel(name, loc)
        hotel.save_to_file()
        return hotel

    @staticmethod
    def delete_hotel(hotel):
        """Deletes hotel data file."""
        os.remove(hotel.filename)

    def display_information(self):
        """Returns hotel information as a string."""
        return f"Hotel Name: {self.name}, loc: {self.loc}"

    def modify_information(self, n_name=None, n_loc=None):
        """Modifies hotel information and updates the file."""
        if n_name:
            self.name = n_name
        if n_loc:
            self.loc = n_loc
        self.save_to_file()

    def r_r(self, reser_id, customer_id, rn, start_date, end_date):
        """Reserve a room if available."""
        con = (room for room in self.rs if room.rn == rn and room.available)
        room = next(con, None)
        if room:
            room.make_reservation()
            reservation = make_reservation(
                reser_id=reser_id,
                customer_id=customer_id,
                hotel_name=self.name,
                rn=rn,
                start_date=start_date,
                end_date=end_date
            )
            reservation.save_to_file()
            self.save_to_file()
            return True
        return False

    def cancel_reservation(self, reser_id):
        """Cancel a room reservation."""
        # This assumes reservation data includes the room number
        try:
            with open(f"reser_{reser_id}.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
            rn = data['rn']
            room_con = (room for room in self.rs if room.rn == rn)
            room = next(room_con, None)
            if room:
                room.cancel_reservation()
                os.remove(f"reservation_{reser_id}.json")
                self.save_to_file()
                return True
        except FileNotFoundError:
            pass
        return False
