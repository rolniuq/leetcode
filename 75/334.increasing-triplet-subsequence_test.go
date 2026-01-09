package lc

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_increasingTriplet(t *testing.T) {
	res := increasingTriplet([]int{20, 100, 10, 12, 5, 13})
	require.Equal(t, true, res)
}
