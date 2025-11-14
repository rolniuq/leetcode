package leetcode

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_generateParenthesis(t *testing.T) {
	res := generateParenthesis(3)
	require.NotNil(t, res)
}
