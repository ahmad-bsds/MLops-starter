from settings import load_env_variable
import hopsworks


def load_dataset_from_feature_store(feature_view_version=1):
    project = hopsworks.login(
        api_key_value=load_env_variable("FS_API_KEY"), project=load_env_variable("FS_PROJECT_NAME")
    )

    fs = project.get_feature_store(
        name="energydemandforcasting_featurestore",
    )

    fg = fs.get_feature_group('customers_segmentation', version=1)

    selected_features = fg.select(
        ['age', 'job', 'marital', 'education', 'default', 'balance',
         'housing', 'loan', 'contact', 'day', 'month', 'duration',
         'campaign', 'pdays', 'previous', 'poutcome', 'y', 'id']
    )

    feature_view = fs.get_or_create_feature_view(
        name='customer_segmentation_view_',
        version=feature_view_version,
        query=selected_features,
        labels=["y"] # target variable
    )

    return feature_view.train_test_split(
        description='transactions fraud training dataset',
        test_size=0.2,
    )


# X_train, X_test, y_train, y_test = load_dataset_from_feature_store()
#
# print("................X Training............")
# print(X_train)
# print("................X testing................")
# print(X_test)
#
# print("................y Training............")
# print(y_train)
# print("................y testing................")
# print(y_test)
