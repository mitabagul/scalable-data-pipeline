from pathlib import Path
import yaml

from src.extract import read_csv

from src.transform import transform_orders

from src.load import write_csv

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

    processed_dir = Path(cfg["data_paths"]["processed_data"])
    out_file = cfg["files"]["processed_output"]
    output_path = processed_dir / out_file
    
    written_path = write_csv(clean_df, output_path)

    print("Loaded rows:", len(result.df))
    print("Clean rows:", len(clean_df))
    print("Wrote processed file to:", written_path)
    print(clean_df.head())

if __name__ == "__main__":
    main()
