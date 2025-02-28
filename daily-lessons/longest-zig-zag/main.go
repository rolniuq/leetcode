package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}

func dfs(root *TreeNode, right bool, counter int) int {
	if root == nil {
		return counter
	}

	if right {
		return max(dfs(root.Left, false, counter+1), dfs(root.Right, true, 0))
	}

	return max(dfs(root.Left, false, 0), dfs(root.Right, true, counter+1))
}

func longestZigZag(root *TreeNode) int {
	return max(dfs(root.Left, false, 0), dfs(root.Right, true, 0))
}

func main() {}
