# customer.py
class Customer:
    """
    Represents a customer in the delivery management system.
    
    Attributes:
        __customer_id (str): Unique identifier for the customer.
        __name (str): The customer's full name.
        __address (str): Residential or shipping address.
        __email (str): Email address used for notifications.
        __phone (str): Contact phone number.
    """
    
    def __init__(self, customer_id, name, address, email, phone):
        self.__customer_id = customer_id
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone

    # --- Getters ---
    def get_customer_id(self):
        return self.__customer_id
    
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_email(self):
        return self.__email
    
    def get_phone(self):
        return self.__phone
    
    # --- Setters ---
    def set_name(self, name):
        self.__name = name
    
    def set_address(self, address):
        self.__address = address
    
    def set_email(self, email):
        self.__email = email
    
    def set_phone(self, phone):
        self.__phone = phone
    
    # --- Example Stub Methods ---
    def validate_contact_details(self):
        """
        Checks if the customer's email and phone number formats
        are valid. Currently just a placeholder.
        """
        pass

