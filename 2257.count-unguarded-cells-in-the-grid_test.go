package leetcode

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_countUnguarded(t *testing.T) {
	m, n := 4, 6
	guards := [][]int{{0, 0}, {1, 1}, {2, 3}}
	walls := [][]int{{0, 1}, {2, 2}, {1, 4}}
	res := countUnguarded(m, n, guards, walls)
	require.Equal(t, 7, res)
}
