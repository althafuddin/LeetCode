class Solution:
    # def validMountainArray(self, arr):
    #     if len(arr) >= 3:
    #         x = 1
    #         counter=self.validateGrowth(arr, x)
    #         return (self.validateDepth(arr,counter))
            
    #     else:
    #         return False

    def validateGrowth(self, arr, x):
        for i in arr:
                if x < len(arr):
                    if i < arr[x]:
                        x+=1
                    else: 
                        return(x-1)

    def validateDepth(self, arr, x):
        decrement_list=arr[x:]
        x = 1
        for i in decrement_list:
                if x < len(decrement_list):
                    if i > decrement_list[x]:
                        x+=1
                    else:
                        return False
                return True

nums_list = [4,3,2,1,1,2,3,1]
class_instance = Solution()
class_instance.validateGrowth(nums_list, 0)