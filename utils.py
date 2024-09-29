import logging


def get_logger(name: str) -> logging.Logger:
    """
    Creates and configures a logger with the specified name.

    Args:
        name (str): Name of the logger.

    Returns:
        logging.Logger: Configured logger instance.
    """

    # Configure the logging level and format
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Get a logger instance
    logger = logging.getLogger(name)

    return logger


