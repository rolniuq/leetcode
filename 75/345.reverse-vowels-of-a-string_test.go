package lc

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_reverseVowels(t *testing.T) {
	res := reverseVowels("IceCreAm")
	require.Equal(t, "AceCreIm", res)
}
