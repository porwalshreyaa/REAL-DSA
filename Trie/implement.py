from utils.colors import Colors


class Node:
    def __init__(self):
        self.children = {}
        self.end_of_word = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def draw(self, current=None):
        trie_list = []
        if not current:
            current = self.root
        if not current.children:
            return []
        for key in current.children.keys():
            child = current.children[key]
            trie_list.append({key: (self.draw(child), child.end_of_word)})
        return trie_list

    def insert(self, word):
        word = str(word)
        l = len(word)
        current = self.root
        for i in range(l):
            if word[i] not in current.children:
                current.children[word[i]] = Node()
            current = current.children[word[i]]
        current.end_of_word += 1
        return None

    def search(self, word):
        word = str(word)
        l = len(word)
        current = self.root
        for i in range(l):
            if word[i] not in current.children:
                return "Not Found"
            current = current.children[word[i]]
        if current.end_of_word:
            return "Found"
        return "Not Found"

    def get_tail(self, words, prefix, node):
        if node.end_of_word:
            words.append(prefix)
        if node.children == {}:
            return
        for i in node.children.keys():
            self.get_tail(words, str(prefix) + str(i), node.children[i])
        return

    def starts_with(self, word):
        word = str(word)
        l = len(word)
        current = self.root
        for i in range(l):
            if word[i] not in current.children:
                return
            current = current.children[word[i]]
        words = []
        self.get_tail(words, word, current)
        return words

    def delete(self, word):
        word = str(word)
        l = len(word)
        current = self.root
        node_stack = []
        for i in range(l):
            node_stack.append(current)
            if word[i] not in current.children:
                return "Not Found"
            current = current.children[word[i]]
        if not current.end_of_word:
            return "Not Found"
        node_stack.append(current)
        current.end_of_word -= 1
        for i in range(l - 1, -1, -1):
            current = node_stack.pop()
            if not current.end_of_word and current.children == {}:
                del current
        return "Deleted"

    def update(self, test_input):
        old_word, new_word = test_input
        old_word = str(old_word)
        new_word = str(new_word)
        found_and_removed =self.delete(old_word)
        if found_and_removed == "Deleted":
            self.insert(new_word)
            return "Updated"
        return "Not Found"


# test_cases = [
#     ("insert", "shoe", None),
#     ("draw", "", [{'s': ([{'h': ([{'o': ([{'e': ([], 1)}], 0)}], 0)}], 0)}]),
#     ("insert", "search", None),
#     ("search", "search", "Found"),
#     ("search", "shoe", "Found"),
#     ("delete", "search", "Deleted"),
#     ("search", "search", "Not Found"),
#     ("insert", "road", None),
#     ("draw", "", [{'s': ([{'h': ([{'o': ([{'e': ([], 1)}], 0)}], 0)}, {'e': ([{'a': ([{'r': ([{'c': ([{'h': ([], 0)}], 0)}], 0)}], 0)}], 0)}], 0)}, {'r': ([{'o': ([{'a': ([{'d': ([], 1)}], 0)}], 0)}], 0)}]),
#     ("search", "road", "Found"),
#     ("insert", "pineapple", None),
#     ("insert", "pine", None),
#     ("delete", "apple", "Not Found"),
#     ("delete", "pine", "Deleted"),
#     ("update", "pineapple,pinetree", "Updated"),
#     ("search", "pinetree", "Found"),
#     ("insert", "", None),
#     ("insert", "（书、杂志等中区别于图片的）正文，文字材料", None),
#     ("search", "（书、杂志等中区别于图片的）正文，文字材料", "Found"),
#     ("insert", "a-b", None),
#     ("insert", "a!", None),
#     ("insert", "a-", None),
#     ("insert", "showroom", None),
#     ("insert", "sabudana", None),
#     ("starts_with", "s", ['shoe', 'showroom', 'sabudana'])
#     (
#         "insert",
#         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
#         None,
#     ),
#     ("search", "（书、杂志等中区别于图片的）正文，文字材料", "Found"),
#     ("search", "a-b", "Found"),
#     ("search", "a!", "Found"),
#     ("search", "a-", "Found"),
#     (
#         "search",
#         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
#         "Found",
#     ),
# ]

test_cases = [
    ("insert", "shop", None),
    ("insert", "shopping", None),
    ("insert", "show", None),
    ("insert", "showstoper", None),
    ("insert", "show", None),  # duplicate inser
    ("insert", "stop", None),
    ("insert", "hash", None),
    ("insert", "hash", None),  # duplicate inser)s
    ("insert", "air", None),
    ("insert", "airbone", None),
    ("insert", 412202, None),
    ("insert", 4122, None),
    ("insert", "（书、杂志等中区别于图片的）正文，文字材料", None),
    ("search", "（书、杂志等中区别于图片的）正文，文字材料", "Found"),
    ("search", "sharp", "Not Found"),
    ("search", "show", "Found"),
    ("search", "airohub", "Not Found"),
    ("search", "stopping", "Not Found"),
    ("search", "shop", "Found"),
    ("search", "shopping", "Found"),
    ("search", "stoper", "Not Found"),
    ("search", 41204, "Not Found"),
    ("search", 412202, "Found"),
    ("starts_with", "sho", ["shop", "shopping", "show", "showstoper"]),
    ("starts_with", "ai", ["air", "airbone"]),
    ("starts_with", "ha", ["hash"]),
    ("starts_with", 412, ["4122", "412202"]),
    ("delete", "air", "Deleted"),
    ("search", "air", "Not Found"),
    ("delete", "airstrip", "Not Found"),
    ("delete", "（书、杂志等中区别于图片的）正文，文字材料", "Deleted"),
    ("search", "（书、杂志等中区别于图片的）正文，文字材料", "Not Found"),
    ("update", ("hash", "namra"), "Updated"),
    ("search", "namra", "Found"),
    ("search", "hash", "Found"),  # this is breaking, why?
    ("delete", 412202, "Deleted"),
    ("search", 412202, "Not Found"),
    ("delete", "showstoper", "Deleted"),
    ("search", "showstoper", "Not Found"),
    ("delete", "shop", "Deleted"),
    ("search", "shop", "Not Found"),
    ("update", (4122, 412202), "Updated"),
    ("search", 412202, "Found"),
    ("update", ("show", "showstoper"), "Updated"),
    ("search", "showstoper", "Found"),
]


trie = Trie()


def code_runner(test_cases):
    count = 0
    for test_op_str, test_in, test_out in test_cases:
        count += 1
        test_op = getattr(trie, test_op_str)
        result = test_op(test_in)
        print(
            f"Test Case {count}:",
            (
                f"{Colors.GREEN}Passed{Colors.ENDC}"
                if result == test_out
                else f"{Colors.RED}Failed{Colors.ENDC}"
            ),
        )
        # print(f"Test Case {count}:", result, f"{Colors.GREEN}Passed{Colors.ENDC}"
        #         if result == test_out
        #         else f"{Colors.RED}Failed{Colors.ENDC}")
    return


code_runner(test_cases)