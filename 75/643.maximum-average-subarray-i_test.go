package lc

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_findMaxAverage(t *testing.T) {
	res := findMaxAverage([]int{0, 1, 1, 3, 3}, 4)
	require.Equal(t, 2.00000, res)
}
