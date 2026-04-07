class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        s_index , g_index = len(s)-1 , len(g)-1
        happy_children = 0
        g.sort()
        s.sort()
        while  g_index >=0 and s_index >=0  :
            if g[g_index] > s[s_index]:
                g_index -= 1
            else :
                s_index -=1
                g_index -= 1
                happy_children +=1
                #print(f"{g_index}{s_index}")
        return happy_children