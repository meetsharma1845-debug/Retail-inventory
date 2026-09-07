import pandas as pd
import threading
import concurrent.futures
import time
from step2_tree import CategoryNode, dfs_total_stock, bfs_find_product

def setup_inventory_tree():
    store = CategoryNode("Kirana Store Root")
    groceries = CategoryNode("Groceries")
    spices = CategoryNode("Spices")
    
    spices.add_child(CategoryNode("Cardamom", stock=50))
    spices.add_child(CategoryNode("Turmerics", stock=120))
    
    groceries.add_child(spices)
    groceries.add_child(CategoryNode("Basmati Rice", stock=200))
    store.add_child(groceries)
    
    return store

def analyze_sales_chunk(chunk_df):
    # Pandas doing math: total revenue per product in this chunk
    chunk_df['Total_Revenue'] = chunk_df['Quantity'] * chunk_df['Price']
    return chunk_df.groupby('Product')['Total_Revenue'].sum()

def run_pandas_analysis():
    print("-> Starting massive Pandas data analysis...")
    df = pd.read_csv("zobaze_sales_export.csv")
    
    # SAFELY split the data into 4 chunks using pure Pandas (Fixes the IndexError)
    chunk_size = len(df) // 4
    chunks = [df.iloc[i:i + chunk_size].copy() for i in range(0, len(df), chunk_size)]
    
    # DEEP THREADING: Use a ThreadPool to process chunks simultaneously
    final_results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(analyze_sales_chunk, chunks)
        for res in results:
            final_results.append(res)
    
    print("-> Pandas Analysis Complete!")
    
    # Combine the results from all 4 threads to show the final output
    total_sales = pd.concat(final_results).groupby(level=0).sum()
    print("\n--- Final Sales Data ---")
    print(total_sales)
    print("------------------------\n")

def run_tree_analysis(store_root):
    print("-> Starting Tree Traversal (DFS/BFS)...")
    total_spices = dfs_total_stock(store_root)
    print(f"   [DFS] Total items in stock: {total_spices}")
    
    found = bfs_find_product(store_root, "Cardamom")
    print(f"   [BFS] Cardamom found in tree: {found}")
    print("-> Tree Analysis Complete!")

if __name__ == "__main__":
    print("--- HIGH PERFORMANCE RETAIL ANALYZER ---")
    store_tree = setup_inventory_tree()
    
    # MULTITHREADING: Run Pandas and Tree tasks at the exact same time
    start_time = time.time()
    
    thread1 = threading.Thread(target=run_pandas_analysis)
    thread2 = threading.Thread(target=run_tree_analysis, args=(store_tree,))
    
    thread1.start()
    thread2.start()
    
    # Wait for both to finish before moving on
    thread1.join()
    thread2.join()
    
    print(f"--- All tasks completed in {round(time.time() - start_time, 2)} seconds ---")