# delivery_note.py
class DeliveryNote:
    """
    Represents a delivery note/document with details about 
    the order, customer, driver, and delivery specifics.
    
    Attributes:
        __note_id (str): Unique identifier for the note.
        __order (Order): Reference to the order being delivered.
        __driver (DeliveryDriver): The driver handling this delivery.
        __delivery_date (str): Scheduled or actual delivery date.
        __recipient_signature (str): Placeholder for recipient's signature or name upon receiving.
    """
    
    def __init__(self, note_id, order, driver, delivery_date, recipient_signature):
        self.__note_id = note_id
        self.__order = order         # An Order object
        self.__driver = driver       # A DeliveryDriver object
        self.__delivery_date = delivery_date
        self.__recipient_signature = recipient_signature
    
    # Getters
    def get_note_id(self):
        return self.__note_id
    
    def get_order(self):
        return self.__order
    
    def get_driver(self):
        return self.__driver
    
    def get_delivery_date(self):
        return self.__delivery_date
    
    def get_recipient_signature(self):
        return self.__recipient_signature
    
    # Setters
    def set_delivery_date(self, delivery_date):
        self.__delivery_date = delivery_date
    
    def set_recipient_signature(self, signature):
        self.__recipient_signature = signature
    
    def generate_note_details(self):
        # This method can remain if you still want a separate function,
        # but we’ll rely on __str__ for printing directly.
        pass

    def __str__(self):
        """
        Return a multi-section string that resembles the sample
        delivery note layout.
        """
        # We'll use the Customer __str__ and Order __str__ directly
        # to embed their information.
        return (
            "Delivery Note\n"
            "Thank you for using our delivery service! "
            "Please print your delivery receipt and present it upon receiving your items.\n\n"

            f"Recipient Details:\n{self.__order.get_customer()}\n\n"
            
            "Delivery Information:\n"
            f"Order Number: {self.__order.get_order_id()}\n"
            f"Reference Number: {self.__note_id}\n"
            f"Delivery Date: {self.__delivery_date}\n"
            f"Delivery Method: Courier\n"       # Hard-coded example
            f"Package Dimensions: \n"          # Hard-coded example
            f"Total Weight: {self.__order.get_total_weight()}\n\n"              # Hard-coded example

            "Summary of Items Delivered:\n"
            f"{self.__order}\n"
            
            # You can optionally add lines for Subtotal, Taxes, etc.
            # if you store or calculate them in the Order class or elsewhere.
            f"Recipient Signature: {self.__recipient_signature}"
        )