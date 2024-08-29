package main

import "fmt"

// 1

func predictPartyVictory(senate string) string {
	r := []int{}
	d := []int{}

	for i := 0; i < len(senate); i++ {
		cur := string(senate[i])
		if cur == "R" {
			r = append(r, i)
		} else {
			d = append(d, i)
		}
	}

	for len(r) > 0 && len(d) > 0 {
		rIndex := r[0]
		r = r[1:]

		dIndex := d[0]
		d = d[1:]

		if rIndex < dIndex {
			r = append(r, rIndex+len(senate))
		} else {
			d = append(d, dIndex+len(senate))
		}
	}

	if len(r) > 0 {
		return "Radiant"
	}

	return "Dire"
}

func main() {
	fmt.Println(predictPartyVictory("RD"))
}
