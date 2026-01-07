package lc

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_reverseWords(t *testing.T) {
	res := reverseWords("a good   example")
	require.Equal(t, "example good a", res)
}
