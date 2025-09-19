#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def print(self, head: Optional[ListNode]):
        cur = head
        while cur is not None:
            print(cur.val)
            cur = cur.next

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node_list = []
        cur = head
        while cur is not None:
            node_list.append(cur)
            cur = cur.next

        if len(node_list) == 0:
            return head

        k %= len(node_list)
        if k == 0:
            return head

        new_head = node_list[len(node_list) - k]
        new_tail = node_list[len(node_list) - k - 1]
        last = node_list[-1]
        last.next = head
        new_tail.next = None

        return new_head


def run():
    root = Solution()
    root.rotateRight()


# @lc code=end
