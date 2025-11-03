package leetcode

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_climbStairs(t *testing.T) {
	res := climbStairs(3)
	require.Equal(t, 3, res)
}
