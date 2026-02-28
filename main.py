# main.py (Draft Architecture)
from ingestion import fetch_nyc_data


# from cleaning import clean_collision_data  <-- We'll build this next

def run_pipeline():
    # 1. Ingest
    raw_df = fetch_nyc_data(dataset_id="h9gi-nx95", limit=1000)

    if raw_df.empty:
        print("Pipeline aborted: No data retrieved.")
        return

    # 2. Clean (Step 2)
    # clean_df = clean_collision_data(raw_df)

    # 3. Analyze (Step 3)
    # ...


if __name__ == "__main__":
    run_pipeline()