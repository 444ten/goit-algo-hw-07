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

def find_max(root):
    if root is None:
        return None
    
    current = root
    while current.right is not None:
        current = current.right
        
    return current.val

def find_min(root):
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left
        
    return current.val

if __name__ == '__main__':
    root = Node(5)
    keys = [3, 2, 4, 7, 9, 10, 1]
    for key in keys:
        root = insert(root, key)

    max_val = find_max(root)
    print(f"Maximum value: {max_val}")  # Expected: 10

    min_val = find_min(root)
    print(f"Minimum value: {min_val}")  # Expected: 1
    