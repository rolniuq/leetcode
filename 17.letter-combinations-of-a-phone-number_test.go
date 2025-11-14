package leetcode

import (
	"strings"
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_letterCombinations(t *testing.T) {
	res := letterCombinations("23")
	require.NotNil(t, res)
	require.True(t, func() bool {
		expected := []string{"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"}
		for _, item := range res {
			if ok := strings.Contains(strings.Join(expected, ","), item); !ok {
				return false
			}
		}
		return true
	}())
}
