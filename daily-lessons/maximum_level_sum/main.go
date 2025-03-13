package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxLevelSum(root *TreeNode) int {
	queue := []*TreeNode{root}
	max := root.Val
	level := 1
	maxLevel := 1

	for len(queue) > 0 {
		sum := 0
		newQueue := []*TreeNode{}
		for i := 0; i < len(queue); i++ {
			sum += queue[i].Val
			if queue[i].Left != nil {
				newQueue = append(newQueue, queue[i].Left)
			}
			if queue[i].Right != nil {
				newQueue = append(newQueue, queue[i].Right)
			}
		}
		if sum > max {
			max = sum
			maxLevel = level
		}

		queue = newQueue
		level++
	}

	return maxLevel
}
