# delivery_driver.py
class DeliveryDriver:
    """
    Represents a delivery driver assigned to handle deliveries.
    
    Attributes:
        __driver_id (str): Unique identifier for the driver.
        __name (str): Driver's full name.
        __vehicle_type (str): Type of vehicle (car, bike, van, etc.).
        __license_number (str): Driving license number.
        __assigned_orders (list): List of orders currently assigned to the driver.
    """
    
    def __init__(self, driver_id, name, vehicle_type, license_number, assigned_orders):
        self.__driver_id = driver_id
        self.__name = name
        self.__vehicle_type = vehicle_type
        self.__license_number = license_number
        self.__assigned_orders = assigned_orders
    
    # --- Getters ---
    def get_driver_id(self):
        return self.__driver_id
    
    def get_name(self):
        return self.__name
    
    def get_vehicle_type(self):
        return self.__vehicle_type
    
    def get_license_number(self):
        return self.__license_number
    
    def get_assigned_orders(self):
        return self.__assigned_orders
    
    # --- Setters ---
    def set_name(self, name):
        self.__name = name
    
    def set_vehicle_type(self, vehicle_type):
        self.__vehicle_type = vehicle_type
    
    def set_license_number(self, license_number):
        self.__license_number = license_number
    
    def set_assigned_orders(self, orders):
        self.__assigned_orders = orders
    
    # --- Example Stub Methods ---
    def assign_order(self, order):
        """
        Assigns a new order to this driver. 
        In real code, you might do checks to see if they're available.
        """
        self.__assigned_orders.append(order)
    
    def update_location(self):
        """
        Would connect to a GPS or tracking module to update the driver's location.
        """
        pass

