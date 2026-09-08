import pandas as pd

def analyze_sales_chunk(chunk_df):
    chunk_df['Total_Revenue'] = chunk_df['Quantity'] * chunk_df['Price']
    return chunk_df.groupby('Product')['Total_Revenue'].sum()

def get_data_chunks(filepath, num_chunks=4):
    df = pd.read_csv(filepath)
    chunk_size = len(df) // num_chunks
    return [df.iloc[i:i + chunk_size].copy() for i in range(0, len(df), chunk_size)]