import pandas as pd

# trying to split this up so it doesnt crash pc
def do_the_math_for_chunk(chunk_of_data):
    # calculate revenue
    chunk_of_data['total_rev'] = chunk_of_data['qty'] * chunk_of_data['price']
    
    # doing it manually to test something
    results = {}
    
    for index, r in chunk_of_data.iterrows():
        n = r['item_name']
        v = r['total_rev']
        if n in results:
            results[n] = results[n] + v
        else:
            results[n] = v
            
    # turn it back to a series 
    return pd.Series(results)

def chop_data_up(file_loc="data/zobaze_sales_export.csv", how_many_pieces=4):
    print("reading from " + file_loc)
    
    try:
        big_df = pd.read_csv(file_loc)
    except:
        print("oops couldnt find the file. run step 1.")
        return []
        
    cut_size = int(len(big_df) / how_many_pieces)
    pieces_list = []
    
    curr_pos = 0
    while curr_pos < len(big_df):
        end_pos = curr_pos + cut_size
        # grab the slice
        slice_df = big_df.iloc[curr_pos:end_pos].copy()
        pieces_list.append(slice_df)
        
        curr_pos = curr_pos + cut_size
        
    return pieces_list

if __name__ == "__main__":
    s = chop_data_up()
    if len(s) > 0:
        print("checking first piece")
        print(do_the_math_for_chunk(s[0]))