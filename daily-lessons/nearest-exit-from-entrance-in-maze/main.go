package main

func nearestExit(maze [][]byte, entrance []int) int {
	// Initialize the queue and visited set
	queue := [][]int{entrance}
	visited := make(map[[2]int]bool)
	visited[[2]int{entrance[0], entrance[1]}] = true

	// Directions for moving up, down, left, right
	directions := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

	steps := 0

	for len(queue) > 0 {
		size := len(queue)
		for i := 0; i < size; i++ {
			current := queue[0]
			queue = queue[1:]

			// Check if we are at an exit
			if (current[0] != entrance[0] || current[1] != entrance[1]) && (current[0] == 0 || current[0] == len(maze)-1 || current[1] == 0 || current[1] == len(maze[0])-1) {
				return steps
			}

			for _, dir := range directions {
				nextRow := current[0] + dir[0]
				nextCol := current[1] + dir[1]

				if nextRow >= 0 && nextRow < len(maze) && nextCol >= 0 && nextCol < len(maze[0]) && maze[nextRow][nextCol] == '.' && !visited[[2]int{nextRow, nextCol}] {
					queue = append(queue, []int{nextRow, nextCol})
					visited[[2]int{nextRow, nextCol}] = true
				}
			}
		}
		steps++
	}

	return -1 // No exit found
}

func main() {

}
