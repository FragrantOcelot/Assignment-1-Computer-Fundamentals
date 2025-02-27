# main.py
from customer import Customer
from order import Order
from delivery_driver import DeliveryDriver
from delivery_note import DeliveryNote

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
    order_items = {
        "ITM001": {"description": "Wireless Keyboard", "quantity": 1, "unit_price": 100.00},
        "ITM002": {"description": "Wireless Mouse & Pad Set", "quantity": 1, "unit_price": 75.00},
        "ITM003": {"description": "Laptop Cooling Pad", "quantity": 1, "unit_price": 120.00},
        "ITM004": {"description": "Camera Lock", "quantity": 3, "unit_price": 15.00}
    }

    order = Order(
        order_id="DEL123456789",
        customer=cust,
        items=order_items,
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
    print(order)

if __name__ == "__main__":
    main()

