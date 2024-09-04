package main

import (
	"fmt"

	treenode "github.com/rolniuq/mypackage/tree-node"
)

func dfs(root *treenode.TreeNode[int], arr *[]int) {
	if root == nil {
		return
	}

	if root.Left == nil && root.Right == nil {
		*arr = append(*arr, root.Val)
		return
	}

	dfs(root.Left, arr)

	dfs(root.Right, arr)
}

func leafSimilar(root1 *treenode.TreeNode[int], root2 *treenode.TreeNode[int]) bool {
	arr1 := []int{}
	arr2 := []int{}

	dfs(root1, &arr1)
	dfs(root2, &arr2)

	if len(arr1) != len(arr2) {
		return false
	}

	for i := range arr1 {
		if arr1[i] != arr2[i] {
			return false
		}
	}

	return true
}

func main() {
	r1 := &treenode.TreeNode[int]{}
	r1 = r1.Create([]int{3, 5, 1, 6, 2, 9, 8, -1, -1, 7, 4})
	r1.Print()

	fmt.Println()

	r2 := &treenode.TreeNode[int]{}
	r2 = r2.Create([]int{3, 5, 1, 6, 7, 4, 2, -1, -1, -1, -1, -1, -1, 9, 8})
	r2.Print()

	fmt.Println()

	fmt.Println(leafSimilar(r1, r2))
}
