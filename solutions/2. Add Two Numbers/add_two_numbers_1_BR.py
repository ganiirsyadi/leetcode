class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        current_node = self
        result_list = []
        while current_node != None:
            result_list.append(str(current_node.val))
            current_node = current_node.next
        return " -> ".join(result_list)
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node_result = ListNode()
        current_node = node_result
        current_l1_node = l1
        current_l2_node = l2

        current_sum = current_l1_node.val + current_l2_node.val
        carry = current_sum // 10
        current_node.val = current_sum % 10
        current_l1_node = current_l1_node.next
        current_l2_node = current_l2_node.next

        while current_l1_node != None or current_l2_node != None:
            current_node.next = ListNode()
            current_node = current_node.next

            l1_exist = current_l1_node != None
            l2_exist = current_l2_node != None

            if l1_exist and l2_exist:
                current_sum = current_l1_node.val + current_l2_node.val + carry
                current_l1_node = current_l1_node.next
                current_l2_node = current_l2_node.next
            elif l2_exist:
                current_sum = current_l2_node.val + carry
                current_l2_node = current_l2_node.next
            else:
                current_sum = current_l1_node.val + carry
                current_l1_node = current_l1_node.next

            carry = current_sum // 10
            current_node.val = current_sum % 10    

        if carry > 0:
            current_node.next = ListNode(val=carry)

        return node_result

    def listToNode(self, list_:list) -> list:
        result_node = ListNode()
        current_node = result_node
        for i, v in enumerate(list_):
            if i != 0:
                current_node.next = ListNode()
                current_node = current_node.next
            current_node.val = v
        return result_node

solution = Solution()
print(solution.addTwoNumbers(solution.listToNode([9,9,9]), solution.listToNode([3,2,1])))
print(solution.listToNode([1,2,3]))

"""
Runtime: 64 ms, faster than 90.44% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.4 MB, less than 44.29% of Python3 online submissions for Add Two Numbers.
"""