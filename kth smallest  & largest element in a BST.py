#kth smallest in a BST
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def kth_smallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right

# Input
n = int(input())
elements = list(map(int, input().split()))
k = int(input())

# Construct BST
root = None
for element in elements:
    root = insert(root, element)

# Find kth smallest element
result = kth_smallest(root, k)
print(result)



#kth largest in a BST
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if not root:
        return TreeNode(val)
    if val > root.val:
        root.right = insert(root.right, val)
    else:
        root.left = insert(root.left, val)
    return root

def kth_largest(root, k):
    stack = []
    current = root
    
    while True:
        # Traverse to the rightmost node
        while current:
            stack.append(current)
            current = current.right
        
        # Pop the largest node (rightmost) and decrement k
        current = stack.pop()
        k -= 1
        
        # If k becomes 0, return the value of the current node
        if k == 0:
            return current.val
        
        # Move to the left subtree of the current node
        current = current.left

# Input
n = int(input())
elements = list(map(int, input().split()))
k = int(input())

# Construct BST
root = None
for element in elements:
    root = insert(root, element)

# Find kth largest element
result = kth_largest(root, k)
print(result)



