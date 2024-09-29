import hopsworks
import pandas as pd
from great_expectations.core import ExpectationSuite
from hsfs.feature_group import FeatureGroup
from feature_pipeline.settings import load_env_variable


def to_feature_store(
        data: pd.DataFrame,
        validation_expectation_suite: ExpectationSuite,
        feature_group_version: int,
) -> FeatureGroup:
    """
    This function takes in a pandas DataFrame and a validation expectation suite,
    performs validation on the data using the suite, and then saves the data to a
    feature store in the feature store.
    """

    # Connect to feature store.
    project = hopsworks.login(
        api_key_value=load_env_variable("FS_API_KEY"), project=load_env_variable("FS_PROJECT_NAME")
    )

    feature_store = project.get_feature_store()

    # Create feature group.
    marketing_feature_group = feature_store.get_or_create_feature_group(
        name="customers_segmentation",
        version=feature_group_version,
        description="Marketing dataset, source unknown.",
        primary_key=['id'],
        # event_time="datetime_utc",
        online_enabled=False,
        expectation_suite=validation_expectation_suite,
    )



    print(data.head())

    # Upload data.
    marketing_feature_group.insert(
        features=data,
        overwrite=True
    )


    # Add feature descriptions.
    # feature_descriptions = [
    #         {
    #             "name": "age",
    #             "description": "The age of the individual in years."
    #         },
    #         {
    #             "name": "job",
    #             "description": "The type of job held by the individual (e.g., admin, technician, etc.)."
    #         },
    #         {
    #             "name": "marital",
    #             "description": "The marital status of the individual (e.g., single, married, divorced)."
    #         },
    #         {
    #             "name": "education",
    #             "description": "The highest level of education attained by the individual (e.g., primary, secondary, tertiary)."
    #         },
    #         {
    #             "name": "default",
    #             "description": "Indicates if the individual has credit in default (yes or no)."
    #         },
    #         {
    #             "name": "balance",
    #             "description": "The individual's bank balance in euros."
    #         },
    #         {
    #             "name": "housing",
    #             "description": "Indicates if the individual has a housing loan (yes or no)."
    #         },
    #         {
    #             "name": "loan",
    #             "description": "Indicates if the individual has a personal loan (yes or no)."
    #         },
    #         {
    #             "name": "contact",
    #             "description": "The type of communication used to contact the individual (e.g., cellular, telephone)."
    #         },
    #         {
    #             "name": "day",
    #             "description": "The last day of the month when the individual was contacted."
    #         },
    #         {
    #             "name": "month",
    #             "description": "The last month when the individual was contacted (e.g., Jan, Feb, etc.)."
    #         },
    #         {
    #             "name": "duration",
    #             "description": "The duration of the last contact in seconds."
    #         },
    #         {
    #             "name": "campaign",
    #             "description": "The number of contacts performed during this campaign for this individual."
    #         },
    #         {
    #             "name": "pdays",
    #             "description": "The number of days since the client was last contacted from a previous campaign (999 means client was not previously contacted)."
    #         },
    #         {
    #             "name": "previous",
    #             "description": "The number of contacts performed before this campaign for this individual."
    #         },
    #         {
    #             "name": "poutcome",
    #             "description": "The outcome of the previous marketing campaign (e.g., success, failure)."
    #         },
    #         {
    #             "name": "y",
    #             "description": "The target variable indicating whether the individual subscribed to a term deposit (yes or no)."
    #         },
    #         {
    #             "name": "id",
    #             "description": "Artificial ID."
    #         }
    #
    #     ]
    #
    # for description in feature_descriptions:
    #     marketing_feature_group.update_feature_description(
    #         description["name"], description["description"]
    #     )

    """Currently, there is a problem with adding description."""

    return marketing_feature_group


