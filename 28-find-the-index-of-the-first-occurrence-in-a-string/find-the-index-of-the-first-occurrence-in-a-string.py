class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nlen = len(needle)
        hlen = len(haystack)
        for index  in range(hlen - nlen +1) :
            
            if haystack[index] == needle[0]:
                #print(f"{haystack[index : index+nlen]}")
                if haystack[index : index+nlen] == needle :
                    #print(f"{haystack[index : index+nlen]}")
                    return index
        return -1
