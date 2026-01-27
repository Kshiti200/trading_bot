import logging
import os


def get_order_logger(order_type: str):
    """
    Creates a dedicated logger for each order type.

    MARKET orders → logs/market_order.log
    LIMIT orders  → logs/limit_order.log
    """

    os.makedirs("logs", exist_ok=True)

    log_file = f"logs/{order_type.lower()}_order.log"

    logger = logging.getLogger(order_type)

    # Prevent duplicate handlers
    if not logger.handlers:
        handler = logging.FileHandler(log_file, encoding="utf-8")
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger


def get_error_logger():
    """
    Separate logger for errors only.
    """

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("ERROR_LOGGER")

    if not logger.handlers:
        handler = logging.FileHandler("logs/errors.log", encoding="utf-8")
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.ERROR)

    return logger
