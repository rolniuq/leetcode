#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (68.88%)
# Likes:    12308
# Dislikes: 159
# Total Accepted:    1.5M
# Total Submissions: 2.1M
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' + '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# A trie (pronounced as "try") or prefix tree is a tree data structure used to
# efficiently store and retrieve keys in a dataset of strings. There are
# various applications of this data structure, such as autocomplete and
# spellchecker.
#
# Implement the Trie class:
#
#
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie
# (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously
# inserted string word that has the prefix prefix, and false otherwise.
#
#
#
# Example 1:
#
#
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
#
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
#
#
#
# Constraints:
#
#
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 10^4 calls in total will be made to insert, search, and
# startsWith.
#
#
#


# @lc code=start
class TrieNode:
    """A node in the Trie data structure."""

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.

        Args:
        word (str): The word to be inserted.
        """

        # Start at the root node
        node = self.root

        # Iterate over each character in the word
        for char in word:
            # If the character is not a child of the current node, add it
            if char not in node.children:
                node.children[char] = TrieNode()

            # Move to the child node
            node = node.children[char]

        # Mark the end of the word
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Searches for a word in the Trie.

        Args:
        word (str): The word to be searched.

        Returns:
        bool: True if the word is found, False otherwise.
        """

        # Start at the root node
        node = self.root

        # Iterate over each character in the word
        for char in word:
            # If the character is not a child of the current node, return False
            if char not in node.children:
                return False

            # Move to the child node
            node = node.children[char]

        # Return whether the node is the end of a word
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Checks if there is any word in the Trie that starts with the given prefix.

        Args:
        prefix (str): The prefix to be searched.

        Returns:
        bool: True if there is any word that starts with the prefix, False otherwise.
        """

        # Start at the root node
        node = self.root

        # Iterate over each character in the prefix
        for char in prefix:
            # If the character is not a child of the current node, return False
            if char not in node.children:
                return False

            # Move to the child node
            node = node.children[char]

        # If we have iterated over the entire prefix, return True
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
