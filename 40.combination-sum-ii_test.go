package leetcode

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_combinationSum2(t *testing.T) {
	candidates := []int{10, 1, 2, 7, 6, 1, 5}
	target := 8
	res := combinationSum2(candidates, target)
	require.NotNil(t, res)
}
