package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func insert(root *TreeNode, val int) {
	if root.Val > val {
		if root.Left == nil {
			root.Left = &TreeNode{Val: val}
		} else {
			insert(root.Left, val)
		}
	} else {
		if root.Right == nil {
			root.Right = &TreeNode{Val: val}
		} else {
			insert(root.Right, val)
		}
	}
}

func buildTree(arr []int) *TreeNode {
	root := &TreeNode{Val: arr[0]}

	for i := 1; i < len(arr); i++ {
		insert(root, arr[i])
	}

	return root
}

func printTree(root *TreeNode) {
	if root == nil {
		return
	}

	print(root.Val)
	printTree(root.Left)
	printTree(root.Right)
}

func searchBST(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return nil
	}

	if root.Val == val {
		return root
	}

	if root.Val > val {
		return searchBST(root.Left, val)
	} else {
		return searchBST(root.Right, val)
	}
}

func main() {
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	root := buildTree(arr)
	printTree(root)
}
