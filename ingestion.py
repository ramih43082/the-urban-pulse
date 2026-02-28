import pandas as pd
import requests
from typing import Optional


def fetch_nyc_data(dataset_id: str, limit: int = 1000) -> pd.DataFrame:
    """
    Fetches a specified number of records from the NYC Open Data API.

    Args:
        dataset_id (str): The Socrata dataset identifier (e.g., 'h9gi-nx95').
        limit (int): The maximum number of rows to fetch.

    Returns:
        pd.DataFrame: A DataFrame containing the fetched data.
                      Returns an empty DataFrame if the request fails.
    """
    # Socrata API endpoint structure
    url = f"https://data.cityofnewyork.us/resource/{dataset_id}.json"
    params = {"$limit": limit}

    try:
        # Defensive: Always enforce a timeout to prevent hanging pipelines
        response = requests.get(url, params=params, timeout=10)

        # Defensive: Catch HTTP errors (e.g., 404 Not Found, 500 Server Error)
        response.raise_for_status()

        # Defensive: Attempt to parse JSON
        data = response.json()

        if not data:
            print(f"Warning: Request succeeded, but no data was returned for dataset '{dataset_id}'.")
            return pd.DataFrame()

        df = pd.DataFrame(data)
        print(f"Success: Retrieved {len(df)} rows from dataset '{dataset_id}'.")
        return df

    except requests.exceptions.Timeout:
        print(f"Network Error: The request timed out after 10 seconds for dataset '{dataset_id}'.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err} - Please verify the dataset ID '{dataset_id}'.")
    except requests.exceptions.RequestException as req_err:
        print(f"Connection Error: {req_err}")
    except ValueError:
        print(f"Data Error: Received an invalid JSON response from dataset '{dataset_id}'.")

    # Defensive: Always return a consistent type (an empty DataFrame) on failure
    return pd.DataFrame()


# --- For your local testing ---
if __name__ == "__main__":
    # Test with Motor Vehicle Collisions dataset ID
    test_id = "h9gi-nx95"
    print("Initiating test fetch...")
    df_crashes = fetch_nyc_data(dataset_id=test_id, limit=500)

    if not df_crashes.empty:
        print("Data columns preview:", df_crashes.columns.tolist()[:5])