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
            trie_list.append(
                {key: (self.draw(child), child.end_of_word)}
            )
        return trie_list

    def insert(self, word):
        l = len(word)
        current = self.root
        for i in range(l):
            if word[i] not in current.children:
                current.children[word[i]] = Node()
            current = current.children[word[i]]
        current.end_of_word += 1
        return None

    def search(self, word):
        l = len(word)
        current = self.root
        for i in range(l):
            if word[i] not in current.children:
                return "Not Found"
            current = current.children[word[i]]
        if current.end_of_word:
            return f"Found: {current.end_of_word}"
        return "Not Found"
    
    def get_tail(self, words, prefix, node):
        if node.end_of_word:
            words.append(prefix)
        if node.children == {}:
            return
        for i in node.children.keys():
            self.get_tail(words,str(prefix)+str(i),node.children[i])
        return

    def starts_with(self, word):
        l = len(word)
        current = self.root
        for i in range(l):
            if word[i] not in current.children:
                return
            current = current.children[word[i]]
        words =[]
        self.get_tail(words,word,current)
        return words

    def delete(self, word):
        l = len(word)
        current = self.root
        node_stack = []
        for i in range(l):
            node_stack.append(current)
            if word[i] not in current.children:
                return "Not Found"
            current = current.children[word[i]]
        node_stack.append(current)
        if current.end_of_word:
            current.end_of_word -=1
        for i in range(l - 1, -1, -1):
            current = node_stack.pop()
            if not current.end_of_word and current.children == {}:
                del current
            elif current.end_of_word:
                if current.end_of_word > 0:
                    current.end_of_word -= 1
                else:
                    return "Not Found"
                return "Deleted"
            else:
                return "Deleted"
        return "Deleted"

    def update(self, test_input):
        old_word, new_word = test_input.split(",")
        if self.delete(old_word):
            self.delete(old_word)
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
    # ("insert", "（书、杂志等中区别于图片的）正文，文字材料", None),
    # ("search", "（书、杂志等中区别于图片的）正文，文字材料", "Found"),
    # ("insert", "a-b", None),
    # ("insert", "a!", None),
    # ("insert", "a-", None),
    # ("insert", "showroom", None),
    # ("insert", "sabudana", None),
    # ("starts_with", "s", ['shoe', 'showroom', 'sabudana'])
    # (
    #     "insert",
    #     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    #     None,
    # ),
    # ("search", "（书、杂志等中区别于图片的）正文，文字材料", "Found"),
    # ("search", "a-b", "Found"),
    # ("search", "a!", "Found"),
    # ("search", "a-", "Found"),
    # (
    #     "search",
    #     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    #     "Found",
    # ),
# ]

# trie = Trie()
# def code_runner(test_cases):
#     result = []
    
#     for test_op_str, test_in, test_out in test_cases:
#         test_op = getattr(trie, test_op_str)
#         # result.append("Right" if test_op(test_in) == test_out else "Wrong")
#         result.append(test_op(test_in))
#     return result


# output = code_runner(test_cases)
# for k in output:
#     print(k)


# import json
# print(json.dumps())