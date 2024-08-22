/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode* head) {
        ListNode* cur = head;
        int pos = 0;

        // key = ListNode.val, value = position
        unordered_map<ListNode*, int> mappy;

        while (cur != NULL) {
            if (mappy.contains(cur)) {
                return true;
            }

            mappy.insert({cur, pos});
            ++pos;
            cur = cur->next;
        }

        return false;
    }
};