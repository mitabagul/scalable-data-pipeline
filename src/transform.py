"""
Purpose:
Handles data cleaning and transformation logic.
"""

from __future__ import annotations

import pandas as pd


def transform_orders(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply minimal, explicit transformations to the orders dataset.

    Transformations:
    - Standardize column names (lowercase, stripped)
    - Parse order_date to datetime
    - Convert amount to numeric and fill missing with 0.0

    Args:
        df: Raw orders dataframe.

    Returns:
        Cleaned dataframe suitable for downstream loading/analytics.
    """
    out = df.copy()

    # Standardize column names
    out.columns = [c.strip().lower() for c in out.columns]

    # Parse dates (coerce invalid to NaT)
    if "order_date" in out.columns:
        out["order_date"] = pd.to_datetime(out["order_date"], errors="coerce")

    # Clean amount
    if "amount" in out.columns:
        out["amount"] = pd.to_numeric(out["amount"], errors="coerce").fillna(0.0)

        # Basic data quality checks (non-blocking)
    expected_cols = {"order_id", "customer_id", "order_date", "amount"}
    missing = expected_cols - set(out.columns)
    if missing:
        raise ValueError(f"Missing expected columns after transform: {sorted(missing)}")

    return out
