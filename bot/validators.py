def validate_inputs(symbol, side, order_type, quantity, price):
    # Normalize inputs
    side = side.upper()
    order_type = order_type.upper()

    # Validate symbol
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a valid string (e.g., BTCUSDT)")

    # Validate side
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    # Validate order type
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    # Validate quantity
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    # Validate price for LIMIT
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")
        if price <= 0:
            raise ValueError("Price must be greater than 0")

    return True