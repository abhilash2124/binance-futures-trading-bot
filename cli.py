import argparse
import logging

from bot.client import get_client
from bot.orders import place_order
from bot.logging_config import setup_logger
from bot.validators import validate_inputs

setup_logger()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

try:
    args = parser.parse_args()

    args.side = args.side.upper()
    args.type = args.type.upper()

    validate_inputs(args.symbol, args.side, args.type, args.quantity, args.price)

    client = get_client()

    print("\n📤 Order Request:")
    print(vars(args))

    logging.info(
        f"Order Request | Symbol={args.symbol}, Side={args.side}, "
        f"Type={args.type}, Quantity={args.quantity}, Price={args.price}"
    )

    response = place_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\n📥 Order Response:")
    print(response)

    logging.info(f"Response: {response}")

    if "error" in response:
        print("❌ Failed:", response["error"])
        logging.error(f"Order Failed: {response['error']}")
    else:
        print("✅ Order placed successfully!")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice"))

        logging.info("Order placed successfully")

except ValueError as e:
    print(f"❌ Validation Error: {str(e)}")
    logging.error(f"Validation Error: {str(e)}")

except Exception as e:
    logging.exception("Unexpected error occurred")
    print("❌ Unexpected Error occurred. Check logs.")