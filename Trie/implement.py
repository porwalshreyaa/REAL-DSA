class Node:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        l = len(word)
        current = self.root
        for i in range(l):
            if word[i] not in current.children:
                current.children[word[i]] = Node()
            current = current.children[word[i]]
        current.end_of_word = True
        return

    def search(self, word):
        l = len(word)
        current = self.root
        for i in range(l):
            if word[i] not in current.children:
                return "Not Found"
            current = current.children[word[i]]
        if current.end_of_word:
            return word
        return "Not Found"

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
            current.end_of_word = False
        for i in range(l-1,-1,-1):
            current = node_stack.pop()
            if not current.end_of_word and current.children == {}:
                del current
            elif current.end_of_word:
                current.end_of_word = False
                return "Deleted"
            else:
                return "Deleted"
        return "Deleted"
            

    def update(self, old_word, new_word):
        self.delete(old_word)
        self.insert(new_word)
        return f"'{old_word}' updated to '{new_word}'"

test_cases = [
    # (operation, test_input, test_output),
    # (operation, test_input, test_output),
    # (operation, test_input, test_output),
    # (operation, test_input, test_output),
    # (operation, test_input, test_output),
    # (operation, test_input, test_output),
]

# def code_runner(test_cases):
#     result = []
#     for (test_in, test_out) in test_cases:
#         result.append("Right" if function(test_in) == test_out else "Wrong")
#     return result

# print(code_runner(test_cases))

trie = Trie()
trie.insert("shoe")
trie.insert("search")
print(trie.search("search"))
print(trie.search("shoe"))
print(trie.delete("search"))
print(trie.search("search"))