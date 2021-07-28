package main

import "fmt"

func missingNumber(nums []int) int {

	// total := int((float64(len(nums)) / float64(2)) * float64((1 + len(nums))))
	// To prevent complex conversion
	total := ((len(nums) * 10 / 2) * (1 + len(nums)) / 10)
	current := 0

	for i := 0; i < len(nums); i++ {
		current += nums[i]
	}

	return total - current
}

func main() {
	fmt.Println(missingNumber([]int{3, 0, 1}))
}

/*

Ide: misal untuk [0, 5]
maka panjang array = 5 (karena ada 1 angka yang hilang) n = len(arr) = angka max
cara nemuin angka yang hilang:
misal [0, 4]
harusnya kalo lengkap [0,1,2,3,4], sumnya 10
misal yang ilang 3 maka menjadi [0,1,2,4] sumnya 7
yang ilang adalah sum total - sum yang ada
untuk mempercepat ngitung sum total, pake rumus
Sum of n consecutive number = (n / 2)(first number + last number)
*/

/*
Runtime: 16 ms, faster than 86.83% of Go online submissions for Missing Number.
Memory Usage: 6.3 MB, less than 99.35% of Go online submissions for Missing Number.
*/
