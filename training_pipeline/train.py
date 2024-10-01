import joblib

from data import load_dataset_from_feature_store
from model import processing_pipeline
from comet_ml import Experiment, Artifact
from comet_ml.integration.sklearn import log_model
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score
import fire
from utils import get_logger, save_model

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
    model = pipeline.fit(X_train, y_train)

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

    experiment.log_metric('classification_accuracy', metric(y_test, model.predict(X_test)))
    experiment.log_confusion_matrix(y_test, model.predict(X_test))
    logger.info("Successfully evaluated model.")

    # Save model:
    logger.info("Saving model...")
    save_model(model["logistic_regression"], "./model.pkl")
    logger.info("Successfully saved model.")

    # Save artifact:
    logger.info("Saving artifact...")
    artifact = Artifact(name="model-alpha", artifact_type="model")
    artifact.add("./model.pkl")
    experiment.log_artifact(artifact)
    logger.info("Successfully saved artifact.")

    # Log model:
    logger.info("Logging model...")
    experiment.log_model("model-alpha", "./model.pkl")
    logger.info("Successfully logged model.")

    # Register model:
    logger.info("Registering model...")
    experiment.register_model("model-alpha")
    logger.info("Successfully registered model.")


if __name__ == '__main__':
    fire.Fire(train)
