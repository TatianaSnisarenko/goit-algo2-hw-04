import unittest
from homework import Homework


class TestHomework(unittest.TestCase):
    def setUp(self):
        # Initialize the Trie with test data
        self.trie = Homework()
        self.words = [
            "apple",
            "application",
            "banana",
            "cat",
            "caterpillar",
            "dog",
            "dodge",
        ]
        for i, word in enumerate(self.words):
            self.trie.put(word, i)

    def test_count_words_with_suffix(self):
        # Test for suffixes that exist
        self.assertEqual(self.trie.count_words_with_suffix("e"), 2)  # apple, dodge
        self.assertEqual(self.trie.count_words_with_suffix("ion"), 1)  # application
        self.assertEqual(self.trie.count_words_with_suffix("a"), 1)  # banana
        self.assertEqual(self.trie.count_words_with_suffix("at"), 1)  # cat

        self.assertEqual(self.trie.count_words_with_suffix("pillar"), 1)  # caterpillar
        # Test for suffixes that do not exist
        self.assertEqual(
            self.trie.count_words_with_suffix("er"), 0
        )  # No words with this suffix

        # Test for an empty suffix
        self.assertEqual(
            self.trie.count_words_with_suffix(""), len(self.words)
        )  # All words

        # Test for case sensitivity
        self.assertEqual(
            self.trie.count_words_with_suffix("E"), 0
        )  # Case-sensitive check

        # Test for invalid input
        with self.assertRaises(TypeError):
            self.trie.count_words_with_suffix(123)  # Non-string input
        with self.assertRaises(TypeError):
            self.trie.count_words_with_suffix(None)  # None as input

    def test_has_prefix(self):
        # Test for prefixes that exist
        self.assertTrue(self.trie.has_prefix("app"))  # apple, application
        self.assertTrue(self.trie.has_prefix("ban"))  # banana
        self.assertTrue(self.trie.has_prefix("ca"))  # cat, caterpillar
        self.assertTrue(self.trie.has_prefix("dog"))  # dog
        self.assertTrue(self.trie.has_prefix("dod"))  # dodge

        # Test for prefixes that do not exist
        self.assertFalse(self.trie.has_prefix("bat"))  # No words with this prefix
        self.assertFalse(self.trie.has_prefix("z"))  # No words with this prefix
        self.assertFalse(
            self.trie.has_prefix("caterpillars")
        )  # Prefix longer than any word

        # Test for an empty prefix
        self.assertTrue(self.trie.has_prefix(""))  # All words have an empty prefix

        # Test for case sensitivity
        self.assertFalse(self.trie.has_prefix("App"))  # Case-sensitive check

        # Test for invalid input
        with self.assertRaises(TypeError):
            self.trie.has_prefix(123)  # Non-string input
        with self.assertRaises(TypeError):
            self.trie.has_prefix(None)  # None as input


if __name__ == "__main__":
    unittest.main()
