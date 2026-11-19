class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        for i in range (min(len(word1), len(word2))):
            merged += word1[i]
            merged += word2[i]
        merged += word1[min(len(word1), len(word2)):]
        merged += word2[min(len(word1), len(word2)):]
        return merged