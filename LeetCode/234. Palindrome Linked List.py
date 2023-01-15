# def isPalindrome(head):
#     """
#     :type head: ListNode
#     :rtype: bool
#     """
#
#     a = head[:len(head) // 2]
#     b = head[len(head):len(head) // 2 + len(head) % 2-1:-1]
#     return True if a == b else False
#
#
# assert isPalindrome([1, 2]) == False
# assert isPalindrome([1, 2, 3, 4]) == False
# assert isPalindrome([1, 2, 3, 4, 5]) == False
# assert isPalindrome([1, 2, 2, 1]) == True
# assert isPalindrome([1, 2, 3, 3, 2, 1]) == True
# assert isPalindrome([1, 2, 3, 4, 2, 1]) == False
# assert isPalindrome([1, 2, 3, 2, 1]) == True


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


obj6 = ListNode(6)
obj5 = ListNode(5,obj6)
obj4 = ListNode(4, obj5)
obj3 = ListNode(3, obj4)
obj2 = ListNode(2, obj3)
obj1 = ListNode(1, obj2)
list_obj = [obj1,obj2,obj3,obj4,obj5,obj6]
list = []
for obj in list_obj:
    list.append(obj.val)
    if obj.next == None:
        break
print(list)
# class Solution(object):
#     def isPalindrome(self, head):
#     a = head[:len(head) // 2]
#     b = head[len(head):len(head) // 2 + len(head) % 2-1:-1]
#     return True if a == b else False
