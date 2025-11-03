package leetcode

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_addBinary(t *testing.T) {
	res := addBinary("11", "1")
	require.Equal(t, "100", res)

	// res := addBinary("1010", "1011")
	// require.Equal(t, "10101", res)
}
