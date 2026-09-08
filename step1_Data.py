import pandas as pd
import random

# generating fake data for testing zobaze pos logic locally
def make_dummy_sales(target_file="data/zobaze_sales_export.csv", row_count=50000):
    print("starting data gen...")
    
    # common items we sell in the shop
    inventory_stuff = [
        "Cardamom 100g", "Basmati Rice 1kg", 
        "Tur Dal Loose", "Lux Soap", 
        "Sugar 1kg", "Tata Tea Gold", "Aashirvaad Atta 5kg"
    ]
    
    row_list = []
    
    for count in range(row_count):
        # building each record manually
        item_chosen = random.choice(inventory_stuff)
        q = random.randint(1, 5)
        p = random.randint(20, 500)
        
        single_record = {
            "txn_id": f"TXN-{1000 + count}",
            "item_name": item_chosen,
            "qty": q,
            "price": p
        }
        row_list.append(single_record)
        
    export_df = pd.DataFrame(row_list)
    export_df.to_csv(target_file, index=False)
    
    print(f"all done. wrote {row_count} lines to {target_file}")

if __name__ == "__main__":
    make_dummy_sales()