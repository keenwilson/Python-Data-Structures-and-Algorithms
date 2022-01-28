class TrieNode:
    def __init__(self, value: str):
        self.value = value
        self.children = [None] * 26
        self.isEndOfWord = False

    def __str__(self):
        return "value=" + self.value


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str):
        current = self.root
        for ch in word:
            index = self.__charToIndex(ch)
            # if we don't have this child, we will create it
            if not current.children[index]:
                current.children[index] = TrieNode(ch)
            # Then point current to that node
            current = current.children[index]

        # After visit all the characters
        # set the last node to end of word
        current.isEndOfWord = True

    def __charToIndex(self, char: str):
        # Private helper function
        # converts key current character into index
        # use only "a" through "z" and lower case
        return ord(char) - ord("a")

    def search(self, word: str):
        # Search word in the trie
        # Return True if word presents in trie
        # else False
        current = self.root
        for ch in word:
            index = self.__charToIndex(ch)
            if not current.children[index]:
                return False
            current = current.children[index]
        return current.isEndOfWord


# driver function
def main():
    keys = ["cat", "can"]

    t = Trie()

    for key in keys:
        t.insert(key)


if __name__ == "__main__":
    main()
