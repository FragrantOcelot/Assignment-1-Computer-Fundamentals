# order.py
class Order:
    """
    Represents a delivery order.
    
    Attributes:
        __order_id (str): Unique identifier for the order.
        __customer (Customer): The customer who made this order.
        __items (list): A list of items (strings, or potentially an Item class).
        __total_price (float): Calculated total price.
        __status (str): Current status of the order (e.g., 'Pending', 'Shipped', 'Delivered').
    """
    
    def __init__(self, order_id, customer, items, total_price, status):
        self.__order_id = order_id
        self.__customer = customer
        self.__items = items
        self.__total_price = total_price
        self.__status = status
    
    # Getters
    def get_order_id(self):
        return self.__order_id
    
    def get_customer(self):
        return self.__customer
    
    def get_items(self):
        return self.__items
    
    def get_total_price(self):
        return self.__total_price
    
    def get_status(self):
        return self.__status
    
    # Setters
    def set_items(self, items):
        self.__items = items
    
    def set_total_price(self, price):
        self.__total_price = price
    
    def set_status(self, status):
        self.__status = status
    
    def calculate_total_price(self):
        """
        Calculates the total price of the order.

        This function should iterate through the list of items in the order,
        multiply the unit price by the quantity for each item, and sum up the 
        total amount.

        Possible implementation steps:
        1. Loop through all items in the order.
        2. Multiply each item's quantity by its unit price.
        3. Sum up the values to compute the total order price.
        4. Update the total_price attribute with the calculated value.
        """
        pass  # Function implementation goes here


    def update_order_status(self, new_status):
        """
        Updates the status of the order.

        This function should modify the order status based on its progress 
        (e.g., "Pending" → "Shipped" → "Delivered"). It may also include 
        checks to prevent invalid status changes.

        Possible implementation steps:
        1. Validate that the new status is a recognized status (e.g., "Pending", 
        "Processing", "Shipped", "Delivered").
        2. Ensure that the status transition is logical (e.g., an order should 
        not move directly from "Pending" to "Delivered").
        3. Update the status attribute with the new value if valid.
        """
        pass  # Function implementation goes here


    def __str__(self):
        """
        Return a summary of items delivered, including 
        quantities/prices if that info is stored here.
        This could match the 'Summary of Items Delivered' table
        in your sample figure.
        """
        # If your `items` are just strings, you can join them.
        # If you have a separate Item class, you might loop and
        # format each item code, description, quantity, etc.
        items_str = "\n".join(self.__items)

        return (
            f"Order ID: {self.__order_id}\n"
            f"Status: {self.__status}\n"
            f"Total Price: AED {self.__total_price}\n"
            "Items:\n"
            f"{items_str}"
        )


