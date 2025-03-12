package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getNodes(root *TreeNode, level int, arr *[]int) {
	if root == nil {
		return
	}

	if len(*arr) == level {
		*arr = append(*arr, root.Val)
	}

	getNodes(root.Right, level+1, arr)
	getNodes(root.Left, level+1, arr)
}

func rightSideView(root *TreeNode) []int {
	var arr []int
	getNodes(root, 0, &arr)
	return arr
}
