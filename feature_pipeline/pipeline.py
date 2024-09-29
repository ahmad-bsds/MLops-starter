import datetime
from typing import Optional
import fire
import pandas as pd
from feature_pipeline.etl import extract_transform, load, validate
from utils import get_logger

logger = get_logger(__name__)


def run(feature_group_version=1) -> dict:
    """
    Extract data from the API, transform it, and load it to the feature store.
    Returns:
          A dictionary containing metadata of the pipeline.
    """
    metadata = {}

    logger.info(f"Extracting data...")
    data = extract_transform.extract_data()
    logger.info("Successfully extracted data from API.")

    logger.info(f"Transforming data.")
    data = extract_transform.transform_data(data)
    logger.info("Successfully transformed data.")

    logger.info("Building validation expectation suite.")
    validation_expectation_suite = validate.build_expectation_suite()
    logger.info("Successfully built validation expectation suite.")

    logger.info(f"Validating data and loading it to the feature store.")

    load.to_feature_store(
        data,
        validation_expectation_suite=validation_expectation_suite,
        feature_group_version=feature_group_version,
    )

    metadata["feature_group_version"] = feature_group_version

    logger.info("Successfully validated data and loaded it to the feature store.")

    logger.info(f"Wrapping up the pipeline.")

    logger.info("Done!")

    return metadata


if __name__ == "__main__":
    fire.Fire(run())
