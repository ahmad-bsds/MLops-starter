from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.compose import make_column_selector
import numpy as np


def processing_pipeline():
    numeric_transformer = StandardScaler()

    def transform_0_1(X):
        return X.replace({'yes': 1, 'no': 0})

    transform_0_1 = FunctionTransformer(transform_0_1)

    processing = ColumnTransformer(
        transformers=[

            ('default', transform_0_1, ['default']),
            ('housing', transform_0_1, ['housing']),
            ('loan', transform_0_1, ['loan']),
            ('onehot', OneHotEncoder(), ['job', 'marital', 'education', 'contact', 'month', 'poutcome']),
            ('num', numeric_transformer, make_column_selector(dtype_include=np.number))
        ],
        remainder='passthrough'
    )

    # Create a pipeline with the preprocessing steps and the logistic regression model
    return Pipeline([
        ('processing', processing),  # Apply the preprocessing steps
        ('logistic_regression', LogisticRegression())  # Fit a logistic regression model
    ])

