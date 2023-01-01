# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        letters = [i for i in pattern]
        if len(words) != len(pattern):
            return False
        if len(set(zip(words, letters))) == len(set(letters)) == len(set(words)):
            return True
        return False
