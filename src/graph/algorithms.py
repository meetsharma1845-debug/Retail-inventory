# building out the category for the shop
class NodeForCategory:
    def __init__(self, cat_name, current_stock=0):
        self.cat_name = cat_name
        self.current_stock = current_stock
        self.sub_cats = []

    def push_child(self, child_obj):
        self.sub_cats.append(child_obj)

def calc_total_inventory(node_item):
    # recursive check to count stock down the tree
    if node_item is None:
        return 0
        
    running_total = node_item.current_stock
    
    for c in node_item.sub_cats:
        running_total += calc_total_inventory(c)
        
    return running_total

def search_product_tree(top_node, what_to_find):
    if not top_node:
        return False
        
    # using a basic list as a queue. pop(0) is slow but works for our scale
    q = [top_node]
    
    while len(q) > 0:
        checking_now = q.pop(0)
        
        # TODO: need to fix case sensitivity later
        if checking_now.cat_name == what_to_find:


            return True
            
        for sub in checking_now.sub_cats:
            q.append(sub)
            
    return False

#  test block
if __name__ == '__main__':
    root = NodeForCategory("Main Shop")
    groc = NodeForCategory("Grocery section")
    clean = NodeForCategory("Cleaning")
    
    s = NodeForCategory("Lux Soap", 15)
    d = NodeForCategory("Tur Dal Loose", 50)

    
    
    clean.push_child(s)
    groc.push_child(d)
    root.push_child(groc)
    root.push_child(clean)
    