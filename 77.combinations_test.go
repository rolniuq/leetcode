package leetcode

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func contains(expected [][]int, item []int) bool {
	for _, exp := range expected {
		if len(exp) != len(item) {
			continue
		}
		match := true
		for i := range exp {
			if exp[i] != item[i] {
				match = false
				break
			}
		}
		if match {
			return true
		}
	}
	return false
}

func Test_combine(t *testing.T) {
	res := combine(4, 2)
	require.True(t, func() bool {
		expected := [][]int{{1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4}}

		for _, item := range res {
			if !contains(expected, item) {
				return false
			}
		}

		return true
	}())
}
