package lc

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_canPlaceFlowers(t *testing.T) {
	res := canPlaceFlowers([]int{1, 0, 0, 0, 0, 0, 1}, 2)
	require.Equal(t, true, res)

	// res := canPlaceFlowers([]int{1, 0, 0, 0, 1, 0, 0}, 2)
	// require.Equal(t, true, res)
}
