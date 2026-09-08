# tracking the shop inventory  
class MyCategoryTree:
    def __init__(self, cat_title, amount_in_stock=0):
        self.cat_title = cat_title
        self.amount_in_stock = amount_in_stock
        self.kids = [] # sub categories come here 

    def stick_child_in(self, kid_node):
        self.kids.append(kid_node)

def figure_out_total_stuff(node_thing):
    if node_thing == None:
        return 0
        
    # start with what is in this exact category
    sum_so_far = node_thing.amount_in_stock
    
    # loop through subcats
    for k in node_thing.kids:
        sum_so_far = sum_so_far + figure_out_total_stuff(k)
        
    return sum_so_far

def go_find_an_item(the_root, search_string):
    if the_root == None:
        return False
        
    # simple list to hold stuff we need to check
    stuff_to_check = [the_root]
    
    while len(stuff_to_check) > 0:
        # grab first one
        current_guy = stuff_to_check[0]
        
        # remove from the list manually
        stuff_to_check = stuff_to_check[1:]
        
        if current_guy.cat_title == search_string:
            return True
            
        for k in current_guy.kids:
            stuff_to_check.append(k)
            
    return False

if __name__ == '__main__':
    # check it works
    r = MyCategoryTree("kirana main")
    g = MyCategoryTree("grocery")
    c = MyCategoryTree("cleaning stuff")
    
    s = MyCategoryTree("Lux Soap", 15)
    d = MyCategoryTree("Tur Dal Loose", 50)
    
    c.stick_child_in(s)
    g.stick_child_in(d)
    r.stick_child_in(g)
    r.stick_child_in(c)
