import logging
import joblib


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


def save_model(model, model_path="/"):
    """
    Template for saving a model.

    Args:
        model: Trained model.
        model_path: Path to save the model.
    """

    joblib.dump(model, model_path)


def load_model(model_path="./training_pipeline/model.pkl"):
    """
    Template for loading a model.

    Args:
        model_path: Path to load the model.
    """

    return joblib.load(model_path)

