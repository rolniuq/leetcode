package main

import (
	"fmt"

	treenode "github.com/rolniuq/mypackage/tree-node"
)

func pathSum(root *treenode.TreeNode[int], targetSum int) int {
	if root == nil {
		return 0
	}

	mapCounter := map[int]int{}
	mapCounter[0] = 1

	return dfs(root, 0, targetSum, mapCounter)
}

func dfs(node *treenode.TreeNode[int], curSum, targetSum int, mapCounter map[int]int) int {
	if node == nil {
		return 0
	}

	curSum += node.Val

	count := mapCounter[curSum-targetSum]
	mapCounter[curSum]++

	count += dfs(node.Left, curSum, targetSum, mapCounter)
	count += dfs(node.Right, curSum, targetSum, mapCounter)

	mapCounter[curSum]--

	return count
}

func main() {
	tree := &treenode.TreeNode[int]{}
	tree = tree.Create([]int{10, 5, -3, 3, 2, -1, 11, 3, -2, -1, 1})

	fmt.Println(pathSum(tree, 8))
}
