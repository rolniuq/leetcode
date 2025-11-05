package leetcode

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_uniquePaths(t *testing.T) {
	res := uniquePaths(3, 7)
	require.Equal(t, 28, res)

	res = uniquePaths(3, 2)
	require.Equal(t, 3, res)
}
