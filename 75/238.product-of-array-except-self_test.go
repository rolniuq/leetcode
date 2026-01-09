package lc

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_productExceptSelf(t *testing.T) {
	res := productExceptSelf([]int{1, 2, 3, 4})
	require.Equal(t, []int{24, 12, 8, 6}, res)
}
