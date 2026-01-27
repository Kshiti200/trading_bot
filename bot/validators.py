def validate_inputs(symbol, side, order_type, quantity, price):
    """
    Validates CLI input before placing an order.
    Raises clear errors if something is wrong.
    """

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be either BUY or SELL.")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

    if order_type == "LIMIT":
        if price is None:
            raise ValueError("LIMIT orders require a price.")
        if price <= 0:
            raise ValueError("Price must be greater than 0.")

    return True
