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

    # Getters
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
    
    # Setters
    def set_name(self, name):
        self.__name = name
    
    def set_address(self, address):
        self.__address = address
    
    def set_email(self, email):
        self.__email = email
    
    def set_phone(self, phone):
        self.__phone = phone
    

    def validate_contact_details(self):
        """
        Validates the customer's contact details.

        This function should check if the email address is in a valid format
        (e.g., contains '@' and a domain name) and if the phone number 
        consists only of digits with an appropriate length. 

        Possible implementation steps:
        1. Ensure the email contains an '@' symbol and a valid domain.
        2. Ensure the phone number is numeric and meets length requirements.
        3. Return True if both validations pass, otherwise return False.
        """
        pass  


    def __str__(self):
        """
        Return recipient (customer) details in a user-friendly format.
        For example, matching the top box in the sample figure
        under 'Recipient Details'.
        """
        return (
            f"Name: {self.__name}\n"
            f"Contact: {self.__email}\n"
            f"Delivery Address: {self.__address}"
        )

