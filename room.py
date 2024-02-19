"""
Module for managing room entities in a hotel reservation system.

Author: Jessica Pulido
Last edited: February 18, 2024
"""


class Room:
    """Represents a room in a hotel.

    Attributes:
        rn (int): The room number.
        room_type (str): The type of the room (e.g., single, double, suite).
        available (bool): Availability status of the room.
        price (float): Price per night for the room.
    """

    def __init__(self, rn, room_type, price, available=True):
        """Initializes a Room with number, type, price, and availability.
           Initially, all rooms are available.

        Parameters:
            rn (int): The room number.
            room_type (str): The type of the room.
            price (float): Price per night for the room.
            available (bool): Availability status of the room.
        """
        self.rn = rn
        self.room_type = room_type
        self.price = price
        self.available = available

    def make_reservation(self):
        """Marks the room as reserved (not available)."""
        self.available = False

    def cancel_reservation(self):
        """Marks the room as available (cancels reservation)."""
        self.available = True

    def update_price(self, new_price):
        """Updates the room's price.

        Parameters:
            new_price (float): The new price of the room.
        """
        self.price = new_price

    @classmethod
    def from_dict(cls, data):
        """Creates a Room instance from a dictionary.

        Parameters:
            data (dict): A dictionary containing room properties.

        Returns:
            Room: An instance of the Room class.
        """
        return cls(
            rn=data['rn'],
            room_type=data['room_type'],
            price=data['price'],
            available=data.get('available', True)
        )

    def to_dict(self):
        """
        Converts the Room instance into a dictionary representation.

        This method allows the Room object's current state to be represented
        as a dictionary, making it easier to serialize, especially for saving
        the room data in formats like JSON.

        Returns:
            dict: A dictionary containing the room's properties, including
                'rn', 'room_type', 'price', and 'available'.
        """
        return {
            'rn': self.rn,
            'room_type': self.room_type,
            'price': self.price,
            'available': self.available
        }
