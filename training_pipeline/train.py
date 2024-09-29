from data import load_dataset_from_feature_store
from model import processing_pipeline


def train():
    X_train, X_test, y_train, y_test = load_dataset_from_feature_store()
    pipe = processing_pipeline()

    # Fit
    return pipe.fit(X_train, y_train)


def comet_ml():
    pass

# Use class for all code here.
