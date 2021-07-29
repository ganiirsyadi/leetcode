package main

func main() {}

func maxSubArray(nums []int) (overallMax int) {
	currentMax := 0
	overallMax = -100000 - 1
	for i := 0; i < len(nums); i++ {
		currentMax += nums[i]
		if currentMax > overallMax {
			overallMax = currentMax
		}
		// kalau sumnya jadi negatif
		// 1. Karena ketemu angka negatif yang gede
		// 2. belum ketemu angka non negatif, artinya ngecek angka negatif mana yang terbesar
		// 		currentMax direset trs ambil angka negatif yang terbesar
		if currentMax < 0 {
			currentMax = 0
		}
	}
	return
}

/*
Runtime: 4 ms, faster than 96.38% of Go online submissions for Maximum Subarray.
Memory Usage: 3.2 MB, less than 38.29% of Go online submissions for Maximum Subarray.
*/
