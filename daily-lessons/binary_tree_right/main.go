package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getLeftRight(root *TreeNode, arr [][]int) {
	if root == nil {
		return
	}

	res := []int{}
	if root.Left != nil {
		res = append(res, root.Left.Val)
	}
	if root.Right != nil {
		res = append(res, root.Right.Val)
	}
	if res == nil {
		return
	}

	arr = append(arr, res)
}

func getLast(arr []int) int {
	return arr[len(arr)-1]
}

func getNodes(root *TreeNode, arr [][]int) {
	if root == nil {
		return
	}

	getLeftRight(root, arr)
	getNodes(root.Left, arr)
	getNodes(root.Right, arr)
}

func rightSideView(root *TreeNode) []int {
	if root == nil {
		return nil
	}

	arr := [][]int{{root.Val}}

	left := root.Left
	right := root.Right
	for left != nil || right != nil {
		if left != nil {
			arr = append(arr, getLeftRight(left))
			left = left.Left
		}
		if right != nil {
			arr = append(arr, getLeftRight(right))
			right = right.Right
		}
	}

	res := []int{}
	for _, v := range arr {
		if len(v) > 0 {
			res = append(res, getLast(v))
		}
	}

	return res
}

func main() {

}
