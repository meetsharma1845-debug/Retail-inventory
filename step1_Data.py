import random
from pathlib import Path

import pandas as pd


# Quick sample dataset for testing inventory logic
# Replace this later with live Zobaze export data when available
def generate_dummy_sales(file_name="data/zobaze_sales_export.csv", num_records=50000):
    print("Generating sample POS data...")

    product_names = [
        "Cardamom 100g",
        "Basmati Rice 1kg",
        "Tur Dal Loose",
        "Lux Soap",
        "Sugar 1kg",
        "Tata Tea Gold",
        "Aashirvaad Atta 5kg",
    ]

    records = []
    for i in range(num_records):
        records.append(
            {
                "txn_id": f"TXN-{1000 + i}",
                "item_name": random.choice(product_names),
                "qty": random.randint(1, 5),
                "price": random.randint(20, 500),  # price in rupees
            }
        )

    output_path = Path(file_name)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    sales_df = pd.DataFrame(records)
    sales_df.to_csv(output_path, index=False)

    print(f"Done. Saved {num_records} rows to {output_path}")


if __name__ == "__main__":
    generate_dummy_sales()