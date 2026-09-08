# System Architecture

This tool is designed to solve processing bottlenecks when handling large retail inventory datasets, specifically focusing on POS exports (like Zobaze) for fast-paced retail and Kirana stores.

## 1. Data Pipeline (Pandas + Deep Threading)
Large CSV transaction logs are too slow to read sequentially. The system divides the dataset into evenly sized chunks and uses Python's `ThreadPoolExecutor`. This allows multiple worker threads to aggregate revenue simultaneously, cutting processing time significantly.

## 2. Inventory Graph (BFS/DFS)
A store's inventory isn't a flat list; it is hierarchical (Store -> Category -> Sub-category -> Item). We model this as a Tree structure:
* **DFS (Depth-First Search):** Used for recursive aggregation. When we need to know the total stock of all items inside the "Spices" branch, DFS explores every sub-branch to the very bottom to calculate the sum.
* **BFS (Breadth-First Search):** Used for level-order searching. When looking for a specific item, BFS checks the top categories first before digging deeper, ensuring the fastest possible lookup time.
