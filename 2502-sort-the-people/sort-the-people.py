class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pair = list(zip(names,heights))
        pair.sort(key=lambda x:x[1],reverse= True)
        #print(pair)
        return [person[0] for person in pair]