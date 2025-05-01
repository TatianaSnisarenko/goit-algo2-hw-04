from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not strings:
            return ""

        # Create a new Trie instance to isolate the current list of strings
        temp_trie = Trie()

        for string in strings:
            temp_trie.put(string)

        current = temp_trie.root
        longest_common_prefix = []

        while current and len(current.children) == 1 and current.value is None:
            # Get the only child node
            char, next_node = next(iter(current.children.items()))
            longest_common_prefix.append(char)
            current = next_node

        return "".join(longest_common_prefix)


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    print("All tests passed.")
