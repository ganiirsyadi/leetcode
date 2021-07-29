/*
  Same but using forloop
*/

package main

import "fmt"

func main() {
	for i := 0; i <= 6; i++ {
		fmt.Println(climbStairs(i))
	}
}

func climbStairs(n int) (result int) {
	// fibo of 1,2,3,5,...
	// for n <= 3
	if n <= 3 {
		return n
	}
	// for n > 3
	lastTwoNumber := 1
	lastOneNumber := 2
	result = 3
	for i := 4; i <= n; i++ {
		lastTwoNumber = lastOneNumber
		lastOneNumber = result
		result = lastOneNumber + lastTwoNumber
	}
	return
}

/*
Runtime: 0 ms, faster than 100.00% of Go online submissions for Climbing Stairs.
Memory Usage: 2 MB, less than 67.56% of Go online submissions for Climbing Stairs.
*/
