package lc

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_maxVowels(t *testing.T) {
	res := maxVowels("aeiou", 2)
	require.Equal(t, 2, res)
}
