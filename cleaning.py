import pandas as pd
import numpy as np
from typing import Optional


def clean_timestamps(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Converts a string column to a standard Python datetime object.

    Args:
        df: The raw DataFrame.
        column_name: The name of the column containing date/time strings.
    """
    # Logic goes here...
    pass


def standardize_coordinates(df: pd.DataFrame, lat_col: str, lon_col: str) -> pd.DataFrame:
    """
    Ensures coordinates are valid floats and removes 'Null Island' (0,0) points.

    Args:
        df: The DataFrame.
        lat_col: Name of the latitude column.
        lon_col: Name of the longitude column.
    """
    # Logic goes here...
    def clean_timestamps(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
        if column_name not in df.columns:
            print(f"Error: Column {column_name} not found.")
            return df

        # errors='coerce' turns unparseable dates into NaT (Not a Time) instead of crashing
        df[column_name] = pd.to_datetime(df[column_name], errors='coerce')

        # Drop rows where the date is completely invalid
        initial_count = len(df)
        df = df.dropna(subset=[column_name])

        print(f"Cleaning Timestamps: Removed {initial_count - len(df)} rows with invalid dates.")
        return df

    def standardize_coordinates(df: pd.DataFrame, lat_col: str, lon_col: str) -> pd.DataFrame:
        # 1. Convert to numeric, forcing errors to NaN
        df[lat_col] = pd.to_numeric(df[lat_col], errors='coerce')
        df[lon_col] = pd.to_numeric(df[lon_col], errors='coerce')

        # 2. Defensive: Remove (0,0) coordinates and NaNs
        # NYC is roughly Lat 40, Lon -74. Anything near 0,0 is an entry error.
        initial_count = len(df)
        mask = (
                df[lat_col].notna() &
                df[lon_col].notna() &
                (df[lat_col] != 0) &
                (df[lon_col] != 0)
        )
        df = df[mask].copy()

        print(f"Cleaning Coordinates: Removed {initial_count - len(df)} rows with invalid GPS data.")
        return df