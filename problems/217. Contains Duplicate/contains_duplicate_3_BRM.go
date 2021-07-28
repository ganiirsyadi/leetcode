package main

func containsDuplicate(nums []int) bool {
	unique_nums := make(map[int]bool)
	for i := 0; i < len(nums); i++ {
		unique_nums[nums[i]] = true
	}
	return len(unique_nums) != len(nums)
}

/*
Runtime: 20 ms, faster than 73.62% of Go online submissions for Contains Duplicate.
Memory Usage: 9 MB, less than 7.54% of Go online submissions for Contains Duplicate.
*/
