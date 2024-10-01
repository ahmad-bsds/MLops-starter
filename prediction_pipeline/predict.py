from utils import get_logger, load_model
import pandas as pd

logger = get_logger(__name__)


# Predict logistic regression model.
def predict(data: pd.DataFrame):
    """
    Predict logistic regression model.
    :param model: model
    :param data: data
    :return: predictions
    """

    logger.info("Loading model...")
    model = load_model()
    logger.info("Successfully loaded model.")

    logger.info("Predicting...")
    model.predict(data)
    logger.info("Successfully predicted.")

    return model.predict(data)


if __name__ == "__main__":
    print(
        predict(
            pd.DataFrame(
                {
                    "age": [1],
                    "job": [1],
                    "marital": [1],
                    "education": [1],
                    "default": [1],
                    "balance": [1],
                    "housing": [1],
                    "loan": [1],
                    "contact": [1],
                    "day": [1],
                    "month": [1],
                    "duration": [1],
                    "campaign": [1],
                    "pdays": [1],
                    "previous": [1],
                    "poutcome": [1],
                }

            )
        )
    )