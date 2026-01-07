package lc

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_kidsWithCandies(t *testing.T) {
	res := kidsWithCandies([]int{4, 2, 1, 1, 2}, 1)
	require.Equal(t, []bool{true, false, false, false, false}, res)
}
