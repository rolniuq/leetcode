package lc

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func Test_compress(t *testing.T) {
	t.Run("test 1", func(t *testing.T) {
		s := []byte("abbbbbbbbbbbb")
		res := compress(s)
		require.Equal(t, 4, res)
	})

	t.Run("test 2", func(t *testing.T) {
		s := []byte("a")
		res := compress(s)
		require.Equal(t, 1, res)
	})

	t.Run("test 3", func(t *testing.T) {
		s := []byte("aabbccc")
		res := compress(s)
		require.Equal(t, 6, res)
	})
}
