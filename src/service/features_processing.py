from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.model_selection import train_test_split

"""
Feature selection:
https://www.datacamp.com/community/tutorials/feature-selection-python
"""


def xgboost(df_raw, independent_features, dependent_feature):
    '''
    https://mljar.com/blog/feature-importance-xgboost/
    Parameters
    ----------
    df
    independent_features
    dependent_feature
    Returns
    -------
    '''

    X = df_raw[independent_features]
    y = df_raw[dependent_feature]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=12)

    from xgboost import XGBRegressor
    xgb = XGBRegressor(n_estimators=100)
    xgb.fit(X_train, y_train)

    #print(xgb.feature_importances_)
    #plt.barh(independent_features, xgb.feature_importances_)
    #sorted_idx = xgb.feature_importances_.argsort()
    #plt.barh(independent_features, xgb.feature_importances_[sorted_idx])
    #plt.title("Visualizing Important Features with Xgboost")
    #plt.show()

    return xgb.feature_importances_, independent_features


def random_forest_regressor(df, independent_features, dependent_feature):
    '''
    https://www.datacamp.com/community/tutorials/random-forests-classifier-python?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034361&utm_targetid=dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1012861&gclid=CjwKCAjwh7H7BRBBEiwAPXjadtOPQq7UfspaKoAcKPiqoHzDlif3GxNN-e55ACwg3fPNVu3ZMefWVhoCHqIQAvD_BwE
    Parameters
    ----------
    df
    independent_features
    dependent_feature

    Returns
    -------
    '''

    X = df[independent_features]
    y = df[dependent_feature]

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    # Create a Gaussian Classifier
    clf = RandomForestRegressor(n_estimators=1000)

    # Train the model using the training sets y_pred=clf.predict(X_test)
    clf.fit(X_train, y_train)
    feature_imp = pd.Series(clf.feature_importances_, index=independent_features).sort_values(ascending=False)

    # Creating a bar plot
    # sns.barplot(x=feature_imp, y=feature_imp.index)
    # Add labels to your graph
    # plt.xlabel('Feature Importance Score')
    # plt.ylabel('Features')
    # plt.title("Visualizing Important Features with Random Forest Classifier")
    # plt.legend()
    # plt.show()

    return feature_imp, feature_imp.index
