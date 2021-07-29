package main

func main() {

}

func singleNumber(nums []int) (result int) {
	result = nums[0]
	for i := 1; i < len(nums); i++ {
		result = result ^ nums[i]
	}
	return
}

// https://yourbasic.org/golang/bitwise-operator-cheat-sheet/

/*
Runtime: 16 ms, faster than 91.27% of Go online submissions for Single Number.
Memory Usage: 6.2 MB, less than 56.62% of Go online submissions for Single Number.
*/
