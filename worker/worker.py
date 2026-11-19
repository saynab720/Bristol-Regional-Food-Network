
import asyncio
import logging
from datetime import date, datetime

from pyzeebe import ZeebeWorker, create_insecure_channel


# --------------------------------------------------
# Configuration
# --------------------------------------------------

CAMUNDA_ADDRESS = "localhost:26500"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# --------------------------------------------------
# Helper functions
# --------------------------------------------------

def parse_date(value):
    """Convert date or date-time strings into date objects."""

    if not isinstance(value, str) or not value.strip():
        raise ValueError("A valid date is required")

    value = value.strip()

    try:
        if "T" in value:
            return datetime.fromisoformat(
                value.replace("Z", "+00:00")
            ).date()

        return date.fromisoformat(value)

    except ValueError:
        raise ValueError(
            f"Invalid date format: {value}. "
            "Use YYYY-MM-DD or an ISO date-time."
        )


def validate_product_data(
    product_id,
    stock_quantity,
    availability_start_date,
    availability_end_date
):
    """Validate product stock and availability information."""

    if not isinstance(product_id, str) or not product_id.strip():
        raise ValueError("Product ID is required")

    if (
        isinstance(stock_quantity, bool)
        or not isinstance(stock_quantity, int)
        or stock_quantity < 0
    ):
        raise ValueError(
            "Stock quantity must be a non-negative integer"
        )

    start_date = parse_date(availability_start_date)
    end_date = parse_date(availability_end_date)

    if end_date < start_date:
        raise ValueError(
            "Availability end date cannot be before start date"
        )

    return start_date, end_date


# --------------------------------------------------
# Main worker
# --------------------------------------------------

async def main():

    logger.info(
        "Connecting to Camunda 8 at %s",
        CAMUNDA_ADDRESS
    )

    channel = create_insecure_channel(
        grpc_address=CAMUNDA_ADDRESS
    )

    worker = ZeebeWorker(channel)

    # 1. Validate product availability information

    @worker.task(task_type="validate-product-availability")
    async def validate_product_availability(
        productId: str,
        stockQuantity: int,
        availabilityStartDate: str,
        availabilityEndDate: str
    ):

        logger.info("Validating product %s", productId)

        start_date, end_date = validate_product_data(
            productId,
            stockQuantity,
            availabilityStartDate,
            availabilityEndDate
        )

        return {
            "productId": productId,
            "stockQuantity": stockQuantity,
            "availabilityStartDate": start_date.isoformat(),
            "availabilityEndDate": end_date.isoformat(),
            "validationSuccessful": True
        }

    # 2. Check available stock quantity

    @worker.task(task_type="check-stock-quantity")
    async def check_stock_quantity(
        stockQuantity: int
    ):

        logger.info(
            "Checking stock quantity: %s",
            stockQuantity
        )

        return {
            "stockQuantity": stockQuantity,
            "hasStock": stockQuantity > 0
        }

    # 3. Mark product as available

    @worker.task(task_type="mark-product-available")
    async def mark_product_available(
        productId: str
    ):

        logger.info(
            "Product %s is available",
            productId
        )

        return {
            "productStatus": "available",
            "isAvailable": True
        }

    # 4. Mark product as out of stock

    @worker.task(task_type="mark-product-out-of-stock")
    async def mark_product_out_of_stock(
        productId: str
    ):

        logger.info(
            "Product %s is out of stock",
            productId
        )

        return {
            "productStatus": "out_of_stock",
            "isAvailable": False
        }

    # 5. Mark product as out of season

    @worker.task(task_type="mark-product-out-of-season")
    async def mark_product_out_of_season(
        productId: str
    ):

        logger.info(
            "Product %s is out of season",
            productId
        )

        return {
            "productStatus": "out_of_season",
            "isAvailable": False
        }

    # 6. Notify producer of updated availability

    @worker.task(task_type="notify-producer-availability")
    async def notify_producer_availability(
        productId: str,
        productStatus: str
    ):

        message = (
            f"Product {productId} availability updated: "
            f"{productStatus}"
        )

        # Simulated notification for this project

        logger.info(
            "PRODUCER NOTIFICATION: %s",
            message
        )

        return {
            "notificationSent": True,
            "notificationMessage": message
        }

    logger.info(
        "Worker started. Waiting for Camunda jobs..."
    )

    try:
        await worker.work()

    finally:
        await channel.close()


# --------------------------------------------------
# Start application
# --------------------------------------------------

if __name__ == "__main__":

    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        logger.info("Worker stopped by user")

    except Exception:
        logger.exception(
            "Worker stopped because of an error"
        )
