class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentences = sentence.split(' ')
        print(sentences)
        for i in range(len(sentences)-1):
            if sentences[i][-1] != sentences[i+1][0]:
                return False
        if sentences[0][0] != sentences[-1][-1]:
            return False
        
        return True