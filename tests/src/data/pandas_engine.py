import pandas as pd


def analyze_sales_chunk(chunk_df):
    chunk_df = chunk_df.copy()
    chunk_df["total_revenue"] = chunk_df["qty"] * chunk_df["price"]
    return chunk_df.groupby("item_name")["total_revenue"].sum()


def get_data_chunks(filepath="data/zobaze_sales_export.csv", num_chunks=4):
    if num_chunks < 1:
        raise ValueError("num_chunks must be at least 1")

    try:
        sales_df = pd.read_csv(filepath)
    except FileNotFoundError:
        print("Couldn't find the sales file. Run step1_Data.py first.")
        return []

    if sales_df.empty:
        print("The sales file is empty.")
        return []

    if len(sales_df) <= num_chunks:
        return [sales_df.copy()]

    chunk_size = max(1, len(sales_df) // num_chunks)
    chunks = [
        sales_df.iloc[i:i + chunk_size].copy()
        for i in range(0, len(sales_df), chunk_size)
    ]

    return chunks


if __name__ == "__main__":
    chunks = get_data_chunks()

    if chunks:
        print("\n--- Revenue by item in the first chunk ---")
        print(analyze_sales_chunk(chunks[0]))