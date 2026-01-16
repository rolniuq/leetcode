package lc

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_maxOperations(t *testing.T) {
	res := maxOperations([]int{1, 2, 3, 4}, 5)
	require.Equal(t, 2, res)

	res = maxOperations([]int{3, 1, 3, 4, 3}, 6)
	require.Equal(t, 1, res)

	res = maxOperations([]int{4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4}, 2)
	require.Equal(t, 2, res)
}
