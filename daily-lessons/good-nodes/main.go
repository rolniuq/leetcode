package main

import (
	"fmt"

	treenode "github.com/rolniuq/mypackage/tree-node"
)

func countGoodNodes(node *treenode.TreeNode[int], maxSoFar int) int {
	if node == nil {
		return 0
	}

	count := 0
	if node.Val >= maxSoFar {
		count = 1
	}

	newMaxSoFar := max(node.Val, maxSoFar)

	count += countGoodNodes(node.Left, newMaxSoFar)
	count += countGoodNodes(node.Right, newMaxSoFar)

	return count
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func goodNodes(root *treenode.TreeNode[int]) int {
	if root == nil {
		return 0
	}

	return countGoodNodes(root, root.Val)
}

func main() {
	tree := &treenode.TreeNode[int]{}
	tree = tree.Create([]int{2, -1, 4, 10, 8, -1, -1, 4})
	tree.Print()

	fmt.Println()

	fmt.Println(goodNodes(tree))
}
