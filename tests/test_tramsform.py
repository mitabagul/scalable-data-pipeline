import pandas as pd

from src.transform import transform_orders


def test_transform_orders_handles_missing_amount():
    df = pd.DataFrame({
        "order_id": [1, 2],
        "customer_id": ["A", "B"],
        "order_date": ["2025-01-01", "2025-01-02"],
        "amount": [10.0, None],
    })

    out = transform_orders(df)

    assert out["amount"].isna().sum() == 0
    assert out.loc[1, "amount"] == 0.0
