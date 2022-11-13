from typing import List, Optional
import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(q, (lst.val, i, lst))

        root = result = ListNode()

        while q:
            node = heapq.heappop(q)
            idx = node[1]
            result.next = node[2]

            result = result.next

            if result.next:
                heapq.heappush(q, (result.next.val, idx, result.next))

        return root.next