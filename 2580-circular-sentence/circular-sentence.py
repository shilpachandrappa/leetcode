class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        last_char = words[-1][-1]
        print(last_char)
        for word in words :
            if last_char != word[0] :
                return False
            last_char = word[-1]
        return True