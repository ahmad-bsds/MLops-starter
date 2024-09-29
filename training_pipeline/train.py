from data import load_dataset_from_feature_store
from model import processing_pipeline
from comet_ml import Experiment
from comet_ml.integration.sklearn import log_model
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score
import fire
from utils import get_logger

logger = get_logger(__name__)


def train():
    # Load dataset
    logger.info("Loading dataset from store...")
    X_train, X_test, y_train, y_test = load_dataset_from_feature_store()
    logger.info("Successfully loaded dataset from store.")
    print(y_train)

    # Build processing pipeline
    logger.info("Processing pipeline...")
    pipeline = processing_pipeline()
    logger.info("Successfully processed pipeline.")

    logger.info("Training model...")
    # Fitting pipeline, training
    pipe = pipeline.fit(X_train, y_train)

    logger.info("Successfully trained model.")

    logger.info("Evaluating model...")
    # Experiment comet ml:
    experiment = Experiment(
        api_key="FkNz3f2PSKFvq6YuUSf3BTJRy",
        project_name="customers-marketing",
        workspace="ahamd-ai"
    )

    # Log metrics
    def metric(y_test, y_pred):
        """
        Calculate a metric for evaluating model performance.

        Parameters
        ----------
        y_test: array-like
            Ground truth target values.
        y_pred: array-like
            Estimated target values.

        Returns
        -------
        A dictionary with the metric name as key and the metric value as value
        """
        return {
            "f1_score": f1_score(y_test, y_pred),
            "precision_score": precision_score(y_test, y_pred),
            "recall_score": recall_score(y_test, y_pred),
            "accuracy_score": accuracy_score(y_test, y_pred)
        }

    experiment.log_metric('classification_accuracy', metric(y_test, pipe.predict(X_test)))

    logger.info("Successfully evaluated model.")

    # Log model
    clf = pipe.named_steps['logistic_regression']
    return log_model(experiment, model=clf, model_name="TheModel")


if __name__ == '__main__':
    fire.Fire(train)
