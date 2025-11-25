/*
 * @lc app=leetcode id=1466 lang=golang
 *
 * [1466] Reorder Routes to Make All Paths Lead to the City Zero
 */
package leetcode

// @lc code=start
func dfs(cur, parent int, graph [][][]int, total *int) {
	for _, edge := range graph[cur] {
		next := edge[0]
		cost := edge[1]

		if next == parent {
			continue
		}

		*total += cost
		dfs(next, cur, graph, total)
	}
}

func minReorder(n int, connections [][]int) int {
	graph := make([][][]int, n)
	for _, pairs := range connections {
		u := pairs[0]
		v := pairs[1]

		graph[u] = append(graph[u], []int{v, 1})
		graph[v] = append(graph[v], []int{u, 0})
	}

	total := 0
	dfs(0, -1, graph, &total)

	return total
}

// @lc code=end
