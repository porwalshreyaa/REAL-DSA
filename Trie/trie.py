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
        word = str(word).lower()
        l = len(word)
        current = self.root
        for i in range(l):
            if word[i] not in current.children:
                current.children[word[i]] = Node()
            current = current.children[word[i]]
        current.end_of_word += 1
        return None

    def search(self, word):
        word = str(word).lower()
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
            self.get_tail(words, str(prefix) + str(i), node.children[i])
        return

    def starts_with(self, word):
        word = str(word).lower()
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
        word = str(word).lower()
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
        old_word = str(old_word).lower()
        new_word = str(new_word).lower()
        found_and_removed =self.delete(old_word)
        if found_and_removed == "Deleted":
            self.insert(new_word)
            return "Updated"
        return "Not Found"