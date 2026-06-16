class BTreeNode:
    def __init__(self, is_leaf= False):
        self.keys = []
        self.children = []
        self.is_leaf = is_leaf

class BTree:
    def __init__(self, order:int):  # order: number of maximum children, min children = order/2
        self.order = order
        self.root = BTreeNode(is_leaf=True)
    
    def insert(self, value:int):
        root = self.root
        # case root is full
        if len(root.keys) == self.order-1: 
            new_root = BTreeNode(is_leaf=False)

            mid = len(root.keys)//2

            right_child = BTreeNode(is_leaf=root.is_leaf)
            mid_value = root.keys[mid]

            new_root.keys.append(mid_value)

            right_child.keys = root.keys[mid+1:]
            root.keys = root.keys[:mid]
            if not root.is_leaf:
                right_child.children = root.children[mid+1:]
                root.children = root.children[:mid+1]
            new_root.children.append(root)
            new_root.children.append(right_child)
            self.root = new_root

        # case root is non full
        root = self.root
        self._insert_non_full(root, value)
        return self.traverse()

    def _insert_non_full(self, node:BTreeNode, value:int):
        # node is non full
        if node.is_leaf:
            i = 0
            while i < len(node.keys):
                if node.keys[i] == value:
                    return
                elif node.keys[i] < value:
                    i +=1
                    continue
                else:
                    break
            node.keys.insert(i, value)
        else:
            i = 0
            while i < len(node.keys):
                if node.keys[i] == value:
                    return
                elif node.keys[i] < value:
                    i +=1
                    continue
                else:
                    break
            if len(node.children[i].keys) == self.order - 1:
                # split child
                pass
            else:
                self._insert_non_full(node.children[i], value)

    
    def _split_child(self):
        pass

    def traverse(self):
        root = self.root
        return self._traverse(root)

    def _traverse(self, node:BTreeNode):
        if node.is_leaf:
            return node.keys
        i = 0
        result = []
        while i < len(node.keys):
            result.extend(self._traverse(node.children[i]))
            result.append(node.keys[i])
            i+=1
        result.extend(self._traverse(node.children[i]))
        return result


# [4, 7, 10]
# [0, 1], [5], [8,9], [12]


testcases = [
    {"input": 1,
    "operation": "insert",
    "expected": [1] },

    {"input": 8,
    "operation": "insert",
    "expected": [1, 8] },
    
    {"input": 0,
    "operation": "insert",
    "expected": [0, 1, 8] },
    
    {"input": 9,
    "operation": "insert",
    "expected": [0, 1, 8, 9] }
]

def run_test():
    tree = BTree(order=4)
    count = 0
    tests = len(testcases)
    for test in testcases:
        if test["operation"] == "search":
            out  = tree.search(test["input"])
            # print(out)
            if out == test["expected"]:
                count +=1
            else:
                print("Test Failed for input:", test["input"])
                return
        elif test["operation"] == "insert":
            out = tree.insert(test["input"])
            print(out)
            if out == test["expected"]:
                count +=1
            else:
                print("Test Failed for input:", test["input"])
        else:
            out = tree.delete(test["input"])
            # print(out)
            if out == test["expected"]:
                count +=1
            else:
                print("Test Failed for input:", test["input"])
    
    print(count, "/", tests, "PASSED")


run_test()