import pandas as pd

# threading crashed on me earlier so we are just slicing the data instead
def process_sales_batch(batch_dataframe):
    # calculating revenue per row first
    batch_dataframe['total_rev'] = batch_dataframe['qty'] * batch_dataframe['price']
    
    # grouping it up by the product name
    grouped_stats = batch_dataframe.groupby('item_name')['total_rev'].sum()
    
    return grouped_stats

def slice_data_up(path_to_csv="data/zobaze_sales_export.csv", splits=4):
    print("fetching from:", path_to_csv)
    
    try:
        raw_pos_data = pd.read_csv(path_to_csv)
    except Exception as e:
        print("failed to load file. did you run the step1 script?")
        return []
        
    size_of_slice = len(raw_pos_data) // splits
    sliced_pieces = []
    
    # using a while loop to slice the dataframe manually
    start_idx = 0
    while start_idx < len(raw_pos_data):
        end_idx = start_idx + size_of_slice
        piece = raw_pos_data.iloc[start_idx:end_idx].copy()
        
        sliced_pieces.append(piece)
        start_idx += size_of_slice
        
    return sliced_pieces

if __name__ == "__main__":
    my_slices = slice_data_up()
    
    if len(my_slices) > 0:
        print("testing slice 0:")
        print(process_sales_batch(my_slices[0]))