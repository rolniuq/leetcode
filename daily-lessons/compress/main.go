package main

import (
	"fmt"
	"strconv"
)

func compress(chars []byte) int {
	writeIndex := 0    // Initializing write index to track the position to write the next character.
	size := len(chars) // Store the size of the input array.

	// Loop over characters in the array starting from the first character.
	for readStart := 0; readStart < size; {
		readEnd := readStart + 1 // Initialize readEnd as the character following readStart.

		// Expand the readEnd pointer to include all consecutive identical characters.
		for readEnd < size && chars[readEnd] == chars[readStart] {
			readEnd++
		}

		// Write the character to the array.
		chars[writeIndex] = chars[readStart]
		writeIndex++

		// If the run of characters is more than one, write the count after the character.
		runLength := readEnd - readStart
		if runLength > 1 {
			runLengthStr := strconv.Itoa(runLength) // Convert runLength to string
			for i := 0; i < len(runLengthStr); i++ {
				chars[writeIndex] = runLengthStr[i]
				writeIndex++
			}
		}

		// Move the readStart to the next unique character.
		readStart = readEnd
	}

	// Return the new length of the array after compression.
	return writeIndex
}

func main() {
	chars := []byte("aabbccc")

	res := compress(chars)
	fmt.Println(res)
}
