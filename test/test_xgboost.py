import unittest
from service.df_preparation import get_init_df
from service.features_processing import xgboost

dependent_feature = ['Revenue']

independent_features = [
    "Gross Profit",
    "Preferred Dividends",
    "Inventory Turnover",
    "Receivables Turnover",
    "Days Payables Outstanding",
    "Stock-based compensation to Revenue"
]


class MyTestCase(unittest.TestCase):

    def test_xgboost(self):
        df_raw, df_encoded = get_init_df("../src/data/financial_data.csv", nrows=100)
        xgboost(df_raw, independent_features, dependent_feature)
        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
