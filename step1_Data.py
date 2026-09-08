import pandas as pd
import random as rnd

def create_my_fake_sales_csv(name_of_file="data/zobaze_sales_export.csv", how_many_rows=50000):
    print("making data now wait a sec...")
    
    my_shop_items = ["Cardamom 100g", "Basmati Rice 1kg", "Tur Dal Loose", "Lux Soap", "Sugar 1kg", "Tata Tea Gold", "Aashirvaad Atta 5kg"]
    
    # making separate lists 
    ids = []
    items = []
    qtys = []
    prices = []
    
    c = 0
    while c < how_many_rows:
        ids.append( "TXN-" + str(1000 + c) )
        items.append( rnd.choice(my_shop_items) )
        qtys.append( rnd.randint(1, 5) )
        prices.append( rnd.randint(20, 500) )
        c = c + 1
        
    # smush it all together in dataframe
    final_table = pd.DataFrame({
        'txn_id': ids,
        'item_name': items,
        'qty': qtys,
        'price': prices
    })
    
    final_table.to_csv(name_of_file, index=False)
    print("ok done. saved " + str(how_many_rows) + " rows.")

if __name__ == '__main__':
    create_my_fake_sales_csv()