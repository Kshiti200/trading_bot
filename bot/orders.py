from bot.logging_config import get_order_logger, get_error_logger

error_logger = get_error_logger()


def place_order(client, symbol, side, order_type, quantity, price=None):
    """
    Places an order on Binance Futures Testnet.

    Logs are stored separately:
    - MARKET → market_order.log
    - LIMIT  → limit_order.log
    """

    # Create logger based on order type
    logger = get_order_logger(order_type)

    try:
        logger.info(
            f"Placing order: Symbol={symbol}, Side={side}, "
            f"Type={order_type}, Quantity={quantity}, Price={price}"
        )

        # MARKET order
        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        # LIMIT order
        elif order_type == "LIMIT":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        else:
            raise ValueError("Unsupported order type.")

        logger.info(f"Order response received: {response}")
        return response

    except Exception as err:
        error_logger.error(f"Order failed: {str(err)}")
        raise
