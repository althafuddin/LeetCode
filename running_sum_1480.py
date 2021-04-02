#Approch1
class Solution:
    def runningSum(self, nums):
        newlist=[]
        tmp=0
        for i in nums:
            tmp+=i 
            newlist.append(tmp)
        return newlist

#nums_list=[1,2,3,4,5]
some_instance = Solution()
print(some_instance.runningSum([1,2,3,4,5]))

#Approch2 - Using itertools
import itertools
class Solution:
    def runningSum(self, nums):
        return list(itertools.accumulate(nums))