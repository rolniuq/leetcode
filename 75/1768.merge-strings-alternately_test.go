package lc

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_mergeAlternately(t *testing.T) {
	res := mergeAlternately("abcd", "pq")
	require.True(t, res == "apbqcd")
}
