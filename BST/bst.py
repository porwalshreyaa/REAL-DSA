class Node:
    def __init__(self, value:int):
        self.value=value
        self.left=None
        self.right=None
# BSTs DO NOT CONTAIN DUPLICATES
class BinarySearchTree:
    def __init__(self, number:int):
        self.root = Node(number)
    def insert(self, number:int):
        curr = self.root
        while True:
            if curr.value == number:
                raise ValueError("Duplicate Value Insertion")
            if curr.value > number and curr.left == None:
                curr.left = Node(number)
                break
            elif curr.value < number and curr.right == None:
                curr.right = Node(number)
                break
            elif curr.value > number:
                curr = curr.left
            else:
                curr = curr.right
    def traverse(self, order):
        if order == "in":
            return "BST Inorder:"+ " ".join(map(str, self.inorder_traversal(self.root)))
        if order == "pre":
            return "BST Preorder:"+ " ".join(map(str, self.preorder_traversal(self.root)))
        if order == "post":
            return "BST Postorder:"+ " ".join(map(str, self.postorder_traversal(self.root)))

    def inorder_traversal(self, parent_node):
        if parent_node == None:
            return ""
        return str(self.inorder_traversal(parent_node.left)) + f" {parent_node.value}"+ str(self.inorder_traversal(parent_node.right))

    def preorder_traversal(self, parent_node):
        if parent_node == None:
            return ""
        return f" {parent_node.value}"+ str(self.preorder_traversal(parent_node.left)) + str(self.preorder_traversal(parent_node.right))

    def postorder_traversal(self, parent_node):
        if parent_node == None:
            return ""
        return str(self.postorder_traversal(parent_node.left)) + str(self.postorder_traversal(parent_node.right)) + f" {parent_node.value}"
    
    def get_min(self, node):
        while node.left:
            node = node.left
        return node
    
    def delete(self, root, value):
        if not root:
            return None
        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            min_node = self.get_min(root.right)
            root.value = min_node.value
            root.right = self.delete(root.right, min_node.value)
        return root





def create_BST(arr:list):
    bst = None
    for i in arr:
        if not bst:
            bst = BinarySearchTree(i)
            continue
        bst.insert(i)
    return bst

test_cases = [
    ("in", [3,8,5,9,1,-20,100,4,2], "BST Inorder: -20 1 2 3 4 5 8 9 100"),
    ("pre", [3,8,5,9,1,-20,100,4,2], "BST Inorder: 3 1 -20 2 8 5 4 9 100"),
    ("post", [3,8,5,9,1,-20,100,4,2], "BST Inorder: -20 2 1 4 5 100 9 8 3")
]

def code_runner():
    result = []
    for test_op, test_in, test_out in test_cases:
        test_bst = create_BST(test_in)
        result.append(test_bst.traverse(test_op)==test_out)
        # result.append(test_bst.traverse(test_op))
    return result

print(code_runner())