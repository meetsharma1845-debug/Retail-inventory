class CategoryNode:
    def __init__(self, name, stock=0):
        self.name = name
        self.stock = stock
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def dfs_total_stock(node):
    if not node:
        return 0
    total = node.stock
    for child in node.children:
        total += dfs_total_stock(child)
    return total

def bfs_find_product(root, target_name):
    if not root:
        return False
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current.name == target_name:
            return True
        for child in current.children:
            queue.append(child)
    return False