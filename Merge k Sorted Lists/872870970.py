# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = []

        while True:
            min = sys.maxsize
            idx = None
            toRemove = None
    
            for i, node in enumerate(lists):
                if node == None:
                    continue

                if node.val < min:
                    min = node.val
                    toRemove = node
                    idx = i
    
            if toRemove == None:
                break

            # print(toRemove.val)

            lists[idx] = toRemove.next
            ans.append(toRemove)

        for i, node in enumerate(ans):
            if i == len(ans) - 1:
                node.next = None
            else:
                node.next = ans[i+1]

        ret = None
        #ret = ans[0]

        for n in ans:
            ret = n
            break

        return ret
        