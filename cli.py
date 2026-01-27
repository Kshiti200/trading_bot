import argparse

from bot.client import BinanceFuturesClient
from bot.orders import place_order
from bot.validators import validate_inputs


def main():
    """
    CLI entry point for the Binance Futures Testnet Trading Bot.
    Users can place MARKET or LIMIT orders using command-line arguments.
    """

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot (Python CLI)"
    )

    # Required arguments
    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol (example: BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"],
        help="Order side"
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT"],
        help="Order type"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order quantity"
    )

    # Optional argument (required for LIMIT)
    parser.add_argument(
        "--price",
        type=float,
        help="Limit price (required only for LIMIT orders)"
    )

    args = parser.parse_args()

    try:
        # Step 1: Validate inputs
        validate_inputs(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        # Step 2: Connect to Binance Futures Testnet
        client = BinanceFuturesClient().client

        # Step 3: Print order summary
        print("\nOrder Request Summary")
        print("----------------------------")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")

        if args.type == "LIMIT":
            print(f"Price    : {args.price}")

        print("\nPlacing order on Binance Futures Testnet...\n")

        # Step 4: Place order
        order = place_order(
            client=client,
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        # Step 5: Print response safely
        if order:
            print("Order Submitted Successfully!")
            print("----------------------------")
            print(f"Order ID     : {order.get('orderId')}")
            print(f"Status       : {order.get('status')}")
            print(f"Executed Qty : {order.get('executedQty')}")
            print(f"Avg Price    : {order.get('avgPrice', 'N/A')}")

            print("\nLog saved in: logs/trading_bot.log\n")
        else:
            print("No response received from Binance API.")

    except Exception as err:
        print("\nOrder Failed!")
        print("----------------------------")
        print("Error:", str(err))
        print("\nCheck logs/trading_bot.log for details.\n")


if __name__ == "__main__":
    main()
