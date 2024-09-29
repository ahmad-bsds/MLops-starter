from great_expectations.core import ExpectationSuite, ExpectationConfiguration
import great_expectations as ge

# List of columns to validate
columns = ['age', 'job', 'marital', 'education', 'default', 'balance',
           'housing', 'loan', 'contact', 'day', 'month', 'duration',
           'campaign', 'pdays', 'previous', 'poutcome', 'y', 'id']


def build_expectation_suite() -> ExpectationSuite:
    """
    Builder used to retrieve an instance of the validation expectation suite.
    """

    expectation_suite_data = ExpectationSuite(
        expectation_suite_name="marketing_exceptions_suite"
    )

    # Columns.
    expectation_suite_data.add_expectation(
        ExpectationConfiguration(
            expectation_type="expect_table_columns_to_match_ordered_list",
            kwargs={
                "column_list": columns
            },
        )
    )

    expectation_suite_data.add_expectation(
        ExpectationConfiguration(
            expectation_type="expect_table_column_count_to_equal", kwargs={"value": 18}
        )
    )

    for column in columns:
        expectation_suite_data.add_expectation(
            ExpectationConfiguration(
                expectation_type="expect_column_values_to_not_be_null",
                kwargs={
                    "column": column
                },
            )
        )

    return expectation_suite_data

# from extract_transform import extract_data, transform_data
#
# data = extract_data()
# data = transform_data(data)
#
# # Load the dataframe into a Great Expectations dataset object
# df_ge = ge.from_pandas(data)
#
# # Build the expectation suite
# expectation_suite = build_expectation_suite()
#
# # Validate the dataset against the expectation suite
# results = df_ge.validate(expectation_suite)
#
# # Output the validation results
# print(results)
