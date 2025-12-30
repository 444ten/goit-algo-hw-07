class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def tree_sum(root):
    if root is None:
        return 0
    
    return root.val + tree_sum(root.left) + tree_sum(root.right)

if __name__ == '__main__':
    root = Node(5)
    
    keys = [3, 2, 4, 7, 9, 10, 1]
    for key in keys:
        root = insert(root, key)

    total_sum = tree_sum(root)
    print(f"Sum of all values: {total_sum}") # 41
    