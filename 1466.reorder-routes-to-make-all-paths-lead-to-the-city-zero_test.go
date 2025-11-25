package leetcode

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_minReorder(t *testing.T) {
	res := minReorder(4, [][]int{{0, 1}, {0, 2}, {3, 2}})
	require.True(t, res == 2)
}
