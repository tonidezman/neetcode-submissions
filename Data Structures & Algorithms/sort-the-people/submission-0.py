class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        x = list(zip(names, heights))
        x.sort(key=lambda x: x[1])
        x.reverse()
        return list(map(lambda x: x[0], x))