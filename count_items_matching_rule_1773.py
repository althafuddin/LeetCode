class Solution:
    def countMatches(self, rulelist, ruleKey, ruleValue):
        x=0
        if ruleKey == "type":
            index = 0
        elif ruleKey == "color":
            index = 1
        else:
            index = 2

        for item in items:
            value = item[index] 
            if value == ruleValue:
                x+=1
        return x       
# class Solution:
#     def countMatches(self, items, ruleKey: str, ruleValue: str) -> int:
#         out =0
#         for i in items:
#             if ruleKey == 'type':
#                 if i[0] == ruleValue:
#                     out = out + 1
#             if ruleKey == 'color':
#                 if i[1] == ruleValue:
#                     out = out +1
#             if ruleKey == 'name':
#                 if i[2] == ruleValue:
#                     out = out + 1
#         return out

items=[
["phone","blue","pixel"],
["computer","silver","lenovo"],
["phone","gold","iphone"]
]

class_instance = Solution()
print(class_instance.countMatches(items,"type","phone"))
