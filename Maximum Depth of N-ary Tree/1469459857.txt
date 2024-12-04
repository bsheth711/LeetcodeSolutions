/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func maxDepth(root *Node) int {
    return dfs(root) 
}

func dfs(node *Node) int {
    if node == nil {
        return 0
    }

    if len(node.Children) == 0 {
        return 1
    }

    best := 0

    for _, child := range node.Children {
        best = max(best, dfs(child) + 1)
    }

    return best
}