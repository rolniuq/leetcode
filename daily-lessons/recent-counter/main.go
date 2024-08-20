package main

import "fmt"

type RecentCounter struct {
	pings []int
}

func Constructor() RecentCounter {
	r := RecentCounter{}
	return r
}

func (this *RecentCounter) Ping(t int) int {
	this.pings = append(this.pings, t)

	for len(this.pings) > 0 && this.pings[0] < t-3000 {
		this.pings = this.pings[1:]
	}

	return len(this.pings)
}

func main() {
	t := 1
	obj := Constructor()
	param_1 := obj.Ping(t)
	fmt.Println(param_1)
	param_2 := obj.Ping(100)
	fmt.Println(param_2)
}
