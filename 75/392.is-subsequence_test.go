package lc

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_isSubsequence(t *testing.T) {
	res := isSubsequence("b", "abc")
	require.Equal(t, true, res)
}
