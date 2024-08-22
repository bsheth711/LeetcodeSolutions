class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # decorate
        decorated = [(-height, name) for name, height in zip(names, heights)]
        # sort
        decorated.sort()
        # undecorate
        return [name for height, name in decorated]