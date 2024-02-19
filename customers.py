"""
Module for managing customer data in the hotel reservation system.

Author: Jessica Pulido
Last edited: February 18, 2024
"""

import json
import os


class Customer:
    """Represents a customer in the hotel reservation system."""

    def __init__(self, c_id, name, email):
        """Initializes a Customer object with c_id, name, and email."""
        self.c_id = c_id
        self.name = name
        self.email = email
        self.filename = f"customer_{c_id}.json"

    def save_to_file(self):
        """Saves customer data to a file."""
        data = {
            'c_id': self.c_id,
            'name': self.name,
            'email': self.email
        }
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    @staticmethod
    def create_customer(c_id, name, email):
        """Creates a new customer and saves it to a file."""
        customer = Customer(c_id, name, email)
        customer.save_to_file()
        return customer

    @staticmethod
    def delete_customer(c_id):
        """Deletes a customer's data file."""
        filename = f"customer_{c_id}.json"
        os.remove(filename)

    def display_customer_info(self):
        """Displays the customer's information."""
        print(f"""Customer c_id: {self.c_id},
              Name: {self.name}, Email: {self.email}""")

    def modify_customer_info(self, name=None, email=None):
        """Modify customer details and saves to file."""
        if name:
            self.name = name
        if email:
            self.email = email
        self.save_to_file()

    @staticmethod
    def load_customer(c_id):
        """Loads a customer's data from a file."""
        filename = f"customer_{c_id}.json"
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return Customer(data['c_id'], data['name'], data['email'])
