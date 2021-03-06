from typing import Any
from layer import Dataset

def build_feature(orders_layer_df: Dataset("orders_dataset")) -> Any:
    # Convert Layer Dataset into pandas data frame
    orders_df = orders_layer_df.to_pandas()

    # Compute a new feature: DAYS_BETWEEN_DELIVERY_AND_PURCHASE --> Days between order delivered date and purchased date
    orders_df["DAYS_BETWEEN_DELIVERY_AND_PURCHASE"] = (orders_df.ORDER_DELIVERED_CUSTOMER_DATE - orders_df.ORDER_PURCHASE_TIMESTAMP).dt.days

    # # Select only the id column and the feature column to be returned
    days_between_delivery_and_purchase = orders_df[['ORDER_ID', 'DAYS_BETWEEN_DELIVERY_AND_PURCHASE']]

    return days_between_delivery_and_purchase
