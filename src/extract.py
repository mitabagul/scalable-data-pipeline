"""
Purpose:
Handles data extraction from source files.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import pandas as pd


@dataclass(frozen=True)
class ExtractResult:
    """Container for extracted dataset and basic metadata."""
    df: pd.DataFrame
    source_path: Path


def read_csv(source_path: Path, *, required_columns: Optional[list[str]] = None) -> ExtractResult:
    """
    Read a CSV file into a DataFrame with minimal validation.

    Args:
        source_path: Path to the CSV file.
        required_columns: Optional list of columns expected to exist.

    Returns:
        ExtractResult containing the DataFrame and source path.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If required columns are missing.
    """
    if not source_path.exists():
        raise FileNotFoundError(f"Input file not found: {source_path}")

    df = pd.read_csv(source_path)

    if required_columns:
        missing = [c for c in required_columns if c not in df.columns]
        if missing:
            raise ValueError(f"Missing required columns: {missing}")

    return ExtractResult(df=df, source_path=source_path)
