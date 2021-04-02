class Solution:
    def defangIPaddr(self, address):
        print(address.replace(".","[.]"))


ip_add = "1.1.1.1"
class_instance = Solution()
class_instance.defangIPaddr(ip_add)