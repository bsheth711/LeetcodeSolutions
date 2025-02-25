/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeNodes(head *ListNode) *ListNode { 
    if head == nil {
        return nil
    }

    cur := head
    writeTo := &ListNode{}
    writeTo.Next = head
    curTotal := 0

    for cur != nil {
        
        if cur.Val == 0 { 
            writeTo = writeTo.Next
            writeTo.Val = curTotal
            curTotal = 0
        } else {
            curTotal += cur.Val
        }

        cur = cur.Next
    }

    writeTo.Next = nil
    head = head.Next

    return head
}