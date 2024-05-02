class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_helper(self.root, val)

    def _insert_helper(self, node, val):
        if val < node.val:
            if node.left:
                self._insert_helper(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self._insert_helper(node.right, val)
            else:
                node.right = TreeNode(val)

    def search(self, target):
        return self._search_helper(self.root, target)

    def _search_helper(self, node, target):
        if not node:
            return False
        if node.val == target:
            return True
        elif target < node.val:
            return self._search_helper(node.left, target)
        else:
            return self._search_helper(node.right, target)

# Main function to read input and perform operations
def main():
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())

    bst = BST()
    for num in nums:
        bst.insert(num)

    if bst.search(target):
        print("Target element is found")
    else:
        print("Target element is not found")

if __name__ == "__main__":
    main()
