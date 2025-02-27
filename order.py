# order.py
class Order:
    """
    Represents a delivery order.
    
    Attributes:
        __order_id (str): Unique identifier for the order.
        __customer (Customer): The customer who made this order.
        __items (dict): A dictionary of items with details (code, description, quantity, unit price).
        __status (str): Current status of the order (e.g., 'Pending', 'Shipped', 'Delivered').
        __total_weight (float): Total weight of the package in kilograms.
        __package_dimensions (str): Package dimensions in the format "LxWxH cm".
    """
    
    def __init__(self, order_id, customer, items, status='OK', total_weight=0.0, package_dimensions="30x20x10 cm"):
        self.__order_id = order_id
        self.__customer = customer
        self.__items = items  # Now a dictionary {item_code: {desc, qty, price}}
        self.__status = status
        self.__total_weight = total_weight
        self.__package_dimensions = package_dimensions

    # --- Getters ---
    def get_order_id(self):
        return self.__order_id
    
    def get_customer(self):
        return self.__customer
    
    def get_items(self):
        return self.__items
    
    def get_status(self):
        return self.__status
    
    def get_total_weight(self):
        return self.__total_weight

    def get_package_dimensions(self):
        return self.__package_dimensions
    
    # --- Setters ---
    def set_items(self, items):
        self.__items = items
    
    def set_status(self, status):
        self.__status = status

    def set_total_weight(self, weight):
        self.__total_weight = weight

    def set_package_dimensions(self, dimensions):
        self.__package_dimensions = dimensions

    # --- Price Calculations ---
    def calculate_subtotal(self):
        """
        Calculates the subtotal by summing (quantity * unit price) for all items.
        """
        return sum(item["quantity"] * item["unit_price"] for item in self.__items.values())

    def calculate_taxes_and_fees(self, tax_rate=0.05):
        """
        Calculates the tax based on a given tax rate (default 5%).
        """
        return self.calculate_subtotal() * tax_rate

    def calculate_total_price(self):
        """
        Calculates the total price including taxes.
        """
        return self.calculate_subtotal() + self.calculate_taxes_and_fees()

    # --- Update Order Status ---
    def update_order_status(self, new_status):
        """
        Updates the status of the order.

        - Ensures that the status transition is logical (e.g., 'Pending' → 'Shipped' → 'Delivered').
        - Can add validation in a real-world system.

        """
        self.__status = new_status

    # --- String Representation ---
    def __str__(self):
        """
        Returns a formatted order summary matching the 'Summary of Items Delivered' table.
        """
        item_lines = [
            f"{code.ljust(8)} {item['description'].ljust(25)} {str(item['quantity']).ljust(8)} {str(item['unit_price']).ljust(10)} {str(item['quantity'] * item['unit_price']).ljust(10)}"
            for code, item in self.__items.items()
        ]

        items_table = "\n".join(item_lines)

        return (
            f"Summary of Items Delivered:\n"
            f"{'Item Code'.ljust(10)} {'Description'.ljust(25)} {'Quantity'.ljust(10)} {'Unit Price (AED)'.ljust(15)} {'Total Price (AED)'}\n"
            f"{'-'*80}\n"
            f"{items_table}\n"
            f"{'-'*80}\n"
            f"Subtotal: AED {self.calculate_subtotal():.2f}\n"
            f"Taxes and Fees: AED {self.calculate_taxes_and_fees():.2f}\n"
            f"Total Charges: AED {self.calculate_total_price():.2f}\n"
        )
