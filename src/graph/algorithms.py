from collections import deque


class CategoryNode:
    def __init__(self, name, stock_qty=0):
        self.name = name
        self.stock_qty = stock_qty
        self.subcategories = []

    def add_subcategory(self, child_node):
        self.subcategories.append(child_node)


def get_total_stock_dfs(node):
    """Return the stock of this category and all its descendants."""
    if not node:
        return 0

    total = node.stock_qty
    for child in node.subcategories:
        total += get_total_stock_dfs(child)

    return total


def find_item_bfs(root_node, search_term):
    """Check whether a category name exists somewhere in the tree."""
    if not root_node:
        return False

    queue = deque([root_node])

    while queue:
        current = queue.popleft()

        if current.name.lower() == search_term.lower():
            return True

        for child in current.subcategories:
            queue.append(child)

    return False


if __name__ == "__main__":
    store = CategoryNode("Main Store")
    grocery = CategoryNode("Groceries")
    cleaning = CategoryNode("Cleaning Supplies")

    soap = CategoryNode("Lux Soap", 15)
    dal = CategoryNode("Tur Dal Loose", 50)

    cleaning.add_subcategory(soap)
    grocery.add_subcategory(dal)
    store.add_subcategory(grocery)
    store.add_subcategory(cleaning)

    print("Total store stock:", get_total_stock_dfs(store))
    print("Do we have Lux Soap?", find_item_bfs(store, "lux soap"))
    print("Do we have Tur Dal Loose?", find_item_bfs(store, "Tur Dal Loose"))