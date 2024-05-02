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

    def inorder_traversal(self):
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.val)
            self._inorder_helper(node.right, result)

# Main function to read input and perform operations
def main():
    n = int(input())
    nums = list(map(int, input().split()))

    bst = BST()
    for num in nums:
        bst.insert(num)

    inorder_result = bst.inorder_traversal()
    print(" ".join(map(str, inorder_result)))

if __name__ == "__main__":
    main()
