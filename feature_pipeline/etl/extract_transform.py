import pandas as pd
import statsmodels.formula.api as sm
import numpy as np


def extract_data(path: str = "D:\B\Portfolio_Projects\Mlops\MLops\data\data_source\data.csv") -> pd.DataFrame:
    """
    Extract data from file.
    :param path: path to data file
    :return: data
    """
    data = pd.read_csv(path, delimiter=';')
    return data


def transform_data(data: pd.DataFrame):
    """
    Transform data.
    :param data: data
    :return: transformed data
    """

    def removes_outlier(df):
        """
        :param df: df
        :return: df without outliers
        """
        # Convert 'y' column to binary values
        df["y"] = df["y"].replace({'yes': 1, 'no': 0})

        df = df.select_dtypes(include=np.number)

        # Remove outliers
        threshold = 4 / len(df)

        dependent_variable = 'y'

        # Create the formula string (excluding the dependent variable from the independent variables)
        formula = dependent_variable + ' ~ ' + ' + '.join(df.drop(dependent_variable, axis=1).columns)

        # Fit the OLS model
        model = sm.ols(formula, data=df).fit()

        # Calculate Cook's distance
        influence = model.get_influence()
        cooks_distance = influence.cooks_distance[0]

        # Add Cook's distance to the dataframe
        df['cooks_distance'] = cooks_distance

        # Remove influential data points from the dataframe
        df = df[df['cooks_distance'] <= threshold]

        # drop distance
        df = df.drop('cooks_distance', axis=1)

        return df

    clean_df = removes_outlier(data)

    data = data.loc[clean_df.index]

    data["y"] = data["y"].replace({'yes': 1, 'no': 0}).astype(int)

    data["loan"] = data["loan"].replace({'yes': 1, 'no': 0}).astype(int)

    data["housing"] = data["housing"].replace({'yes': 1, 'no': 0}).astype(int)

    data["default"] = data["default"].replace({'yes': 1, 'no': 0}).astype(int)

    data["id"] = data.index

    return data

# data = extract_data()
#
# data = transform_data(data)
#
# print(len(data.columns.tolist()))
