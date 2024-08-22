/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* nodeA = l1;
        ListNode* nodeB = l2;
        ListNode* prev = new ListNode();
        ListNode* dummy = prev;
        int carry = 0;
        int sum;

        while (nodeA != nullptr || nodeB != nullptr || carry != 0) {
            cout << carry << "\n";
            sum = carry;
            carry = 0;
            
            if (nodeA != nullptr) {
                sum += nodeA->val;
                nodeA = nodeA->next;
            }
            if (nodeB != nullptr) {
                sum += nodeB->val;
                nodeB = nodeB->next;
            }

            if (sum >= 10) {
                carry = sum / 10;
                sum %= 10;
            }

            ListNode* newNode = new ListNode(sum);
            prev->next = newNode;
            prev = newNode;
        }

        ListNode* head = dummy->next;

        delete(dummy);

        return head;

    }
};