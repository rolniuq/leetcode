package lc

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_gcdOfStrings(t *testing.T) {
	res := gcdOfStrings("AAAAAB", "AAA")
	require.True(t, res == "AAA")
}
