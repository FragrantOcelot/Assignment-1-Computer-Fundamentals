# main.py
from customer import Customer
from order import Order
from delivery_driver import DeliveryDriver
from delivery_note import DeliveryNote

# main.py

def main():
    # Create a Customer
    cust = Customer(
        customer_id="CUST-001",
        name="Sarah Johnson",
        address="45 Knowledge Avenue, Dubai, UAE",
        email="sarah.johnson@example.com",
        phone="123-4567"
    )

    # Create an Order
    order = Order(
        order_id="DEL123456789",
        customer=cust,
        items=["ITM001: Wireless Keyboard (1 x 100.00 AED)",
               "ITM002: Mouse & Pad (1 x 75.00 AED)",
               "ITM003: Laptop Cooling Pad (1 x 120.00 AED)",
               "ITM004: Camera Lock (3 x 15.00 AED)"],
        total_price=283.50,
        status="Delivered",
        total_weight=7,
        package_dimensions="30x20x10 cm"
    )

    driver = DeliveryDriver(
        driver_id="DRVR-001",
        name="John Doe",
        vehicle_type="Car",
        license_number="ABC123",
        delivery_method="Courier",
        assigned_orders=[order]
    )

    # Create the Delivery Note
    note = DeliveryNote(
        note_id="DN-2025-001",
        order=order,
        driver=driver,
        delivery_date="January 25, 2025",
        recipient_signature="Sarah Johnson"
    )

    # Print the delivery note
    print(note)

if __name__ == "__main__":
    main()

