import unittest
from task_two import LongestCommonWord


class TestLongestCommonWord(unittest.TestCase):
    def setUp(self):
        self.trie = LongestCommonWord()

    def test_common_prefix(self):
        # Basic test cases
        strings = ["flower", "flow", "flight"]
        self.assertEqual(self.trie.find_longest_common_word(strings), "fl")

        strings = ["interspecies", "interstellar", "interstate"]
        self.assertEqual(self.trie.find_longest_common_word(strings), "inters")

        strings = ["dog", "racecar", "car"]
        self.assertEqual(self.trie.find_longest_common_word(strings), "")

    def test_empty_input(self):
        # Empty list of strings
        strings = []
        self.assertEqual(self.trie.find_longest_common_word(strings), "")

    def test_single_string(self):
        # Single string in the list
        strings = ["single"]
        self.assertEqual(self.trie.find_longest_common_word(strings), "single")

    def test_identical_strings(self):
        # All strings are identical
        strings = ["test", "test", "test"]
        self.assertEqual(self.trie.find_longest_common_word(strings), "test")

    def test_no_common_prefix(self):
        # No common prefix
        strings = ["abc", "def", "ghi"]
        self.assertEqual(self.trie.find_longest_common_word(strings), "")

    def test_partial_match(self):
        # Partial match
        strings = ["prefix", "prelude", "prevent"]
        self.assertEqual(self.trie.find_longest_common_word(strings), "pre")

    def test_case_sensitivity(self):
        # Case sensitivity
        strings = ["Case", "caseSensitive", "cases"]
        self.assertEqual(self.trie.find_longest_common_word(strings), "")

    def test_special_characters(self):
        # Strings with special characters
        strings = ["@home", "@host", "@hope"]
        self.assertEqual(self.trie.find_longest_common_word(strings), "@ho")

    def test_numeric_strings(self):
        # Strings with numbers
        strings = ["12345", "123", "123abc"]
        self.assertEqual(self.trie.find_longest_common_word(strings), "123")

    def test_mixed_strings(self):
        # Mixed strings
        strings = ["abc123", "abc", "abc456"]
        self.assertEqual(self.trie.find_longest_common_word(strings), "abc")

    def test_long_strings(self):
        # Long strings with a common prefix
        strings = ["a" * 1000 + "b", "a" * 1000 + "c", "a" * 1000 + "d"]
        self.assertEqual(self.trie.find_longest_common_word(strings), "a" * 1000)


if __name__ == "__main__":
    unittest.main()
