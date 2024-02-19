"""
Unit tests for the Customer class.

This module contains tests that verify the functionality of the Customer class,
ensuring that all methods behave as expected under various conditions.
"""

import unittest
import os
import io
from unittest.mock import patch
from customers import Customer


class TestCustomer(unittest.TestCase):
    """Tests for functionality of the Customer class."""
    def setUp(self):
        """Setup method to create a customer instance before each test."""
        self.customer = Customer(c_id=1, name='A', email='ab@e.com')

    def test_customer_initialization(self):
        """Test the initialization of a customer."""
        self.assertEqual(self.customer.c_id, 1)
        self.assertEqual(self.customer.name, 'A')
        self.assertEqual(self.customer.email, 'ab@e.com')

    def test_delete_customer(self):
        """Test deleting a customer removes their data file."""
        # Setup: Create a new customer and ensure their data file exists
        c_id = "cust1001"
        Customer.create_customer(c_id, "A", "ab@e.com")
        expected_filename = f"customer_{c_id}.json"
        self.assertTrue(os.path.exists(expected_filename), "D should exist")

        # Act: Delete the customer
        Customer.delete_customer(c_id)

        # Assert: Verify the customer's data file has been deleted
        self.assertFalse(os.path.exists(expected_filename), "D should be del")

    def test_display_customer_info(self):
        """Test displaying customer information prints the correct details."""
        customer = Customer("cust1002", "B", "bc@e.com")
        expected_output = "Customer id: cust1002,\n Name: B, Email: bc@e.com\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            customer.display_customer_info()
            self.assertEqual(fake_out.getvalue(), expected_output,
                             "Output should match expected customer details")

    def test_update_details(self):
        """Test updating customer's details."""
        new_name = 'B'
        new_email = 'bc@e.com'
        self.customer.modify_customer_info(name=new_name, email=new_email)
        self.assertEqual(self.customer.name, new_name)
        self.assertEqual(self.customer.email, new_email)

    def test_load_customer(self):
        """Test loading a customer retrieves the correct information."""
        # Setup: Create a customer and write their data to a file
        c_id = "cust1003"
        ori = Customer.create_customer(c_id, "C", "cdb@e.com")

        # Act: Load the customer from the file
        load = Customer.load_customer(c_id)

        # Assert: Verify the load customer matches the ori
        self.assertEqual(load.c_id, ori.c_id, "Cus ids should match.")
        self.assertEqual(load.name, ori.name, "Cus names should match.")
        self.assertEqual(load.email, ori.email, "Cus emails should match.")

        # Cleanup: Delete the customer file to clean up test environment
        os.remove(f"customer_{c_id}.json")


if __name__ == '__main__':
    unittest.main()
