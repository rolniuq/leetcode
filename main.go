package main

import "fmt"

func main() {
	w1 := "hello"
	w2 := "he"
	fmt.Println(w1[len(w2):])
}
