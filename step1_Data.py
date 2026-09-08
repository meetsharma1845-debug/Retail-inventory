import pandas as pd
import random
from datetime import datetime, timedelta

def generate_pos_data(filename="zobaze_sales_export.csv", rows=50000):
    print("Generating POS data...")
    products = ["Cardamom", "Basmati Rice", "Tur Dal", "Soap", "Sugar", "Tea Powder"]
    
    data = []
    for i in range(rows):
        data.append({
            "TransactionID": f"TXN-{1000 + i}",
            "Product": random.choice(products),
            "Quantity": random.randint(1, 5),
            "Price": random.randint(20, 500)
        })
    
    # Pandas creates a 'DataFrame' (a digital spreadsheet)
    df = pd.DataFrame(data)
    # Save it to a CSV file
    df.to_csv(filename, index=False)
    print(f"Saved {rows} rows to {filename}")

if __name__ == "__main__":
    generate_pos_data(),ṇ