class Solution:
    def runningSum(self, arr: List[int]) -> List[int]:
               
        for i in range(1, len(arr)):
            arr[i]=arr[i-1]+arr[i]

        return arr
