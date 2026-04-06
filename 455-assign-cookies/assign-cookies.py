class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        gi, si = len(g)-1, len(s)-1
        happy_childern = 0
        g.sort()
        s.sort()
        #print(g)
        #print(s)
        while gi >=0 and si >=0  :
            if g[gi] > s[si]:
                gi -= 1
            else :
                gi -= 1
                si -= 1
                happy_childern += 1
            
        return happy_childern
