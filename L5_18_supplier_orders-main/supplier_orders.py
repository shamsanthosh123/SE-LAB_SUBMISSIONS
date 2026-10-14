"""Track supplier purchase orders and warehouse deliveries."""

import sqlite3


def create_database():
    """Create an in-memory database and its orders table."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """CREATE TABLE orders (
            id INTEGER PRIMARY KEY,
            supplier TEXT,
            item TEXT,
            quantity INTEGER,
            received INTEGER
        )"""
    )
    return connection


def place_order(connection, supplier, item, quantity):
    """Insert an order and return its quantity."""
    connection.execute(
        """INSERT INTO orders (supplier, item, quantity, received)
           VALUES (?, ?, ?, 0)""",
        (supplier, item, quantity),
    )
    return quantity


def mark_received(connection, order_id):
    """Mark the specified order as received."""
    connection.execute(
        "UPDATE orders SET received = 1 WHERE id = ?",
        (order_id,),
    )


def notify_warehouse(supplier):
    """Print a warehouse notification for the supplier."""
    print(f"notifying warehouse about {supplier}")


def cleanup(connection):
    """Remove orders that have already been received."""
    connection.execute("DELETE FROM orders WHERE received = 1")


def pending_count(connection):
    """Return the number of orders that are still pending."""
    result = connection.execute(
        "SELECT COUNT(*) FROM orders WHERE received = 0"
    ).fetchone()
    return result[0]


def main():
    """Run a short demonstration of the purchase-order tracker."""
    connection = create_database()
    order_total = 0
    order_total += place_order(connection, "Acme Steel", "rods", 40)
    order_total += place_order(connection, "Bolt Co", "bolts", 500)
    mark_received(connection, 1)
    notify_warehouse("Acme")
    print(pending_count(connection), order_total)
    cleanup(connection)
    connection.close()


if __name__ == "__main__":
    main()
