class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxEncountered = arr[-1]

        for i in range(len(arr) - 2, -1, -1):
            element = arr[i]
            arr[i] = maxEncountered
            maxEncountered = max(element, maxEncountered)
            
        arr[-1] = -1

        return arr