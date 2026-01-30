from pathlib import Path
import yaml

from src.extract import read_csv

from src.transform import transform_orders

def load_config() -> dict:
    """Load pipeline configuration."""
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)


def main() -> None:
    cfg = load_config()

    raw_dir = Path(cfg["data_paths"]["raw_data"])
    raw_file = cfg["files"]["raw_input"]
    source_path = raw_dir / raw_file

    result = read_csv(
        source_path,
        required_columns=["order_id", "customer_id", "order_date", "amount"]
    )

    clean_df = transform_orders(result.df)

    print("Loaded rows:", len(result.df))
    print("Clean rows:", len(clean_df))
    print(clean_df.head())



if __name__ == "__main__":
    main()
