class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index1, index2 = 0 , 0
        merged = []
        while index1 < len(word1) and index2 < len(word2) :
            merged.append(word1[index1])
            merged.append(word2[index2])
            index1 += 1
            index2 += 1
        while index1 < len(word1) :
            merged.append(word1[index1])
            index1 += 1
        while index2 < len(word2) :
            merged.append(word2[index2])
            index2 += 1
        return "".join(merged)
