from typing import List


class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		value_index_dict = {} # value : index

		# enumerates return index, value pair of a list
		for index, element in enumerate(nums):

			# find other value so that the sum match to target
			diff = target - element
			
			# pada posisi ini diff pasti lebih kecil, 
			# misal target = 5 untuk list [1,4]
			# ketika menemukan 1, pasti 4 belum ada di dict, tetapi ketika menemukan 4, 1 (diff) sudah ada di dict
			# makanya untuk return dibalik, index diff terlebih dahulu baru yang current index
			if diff in value_index_dict:
				return [value_index_dict[diff], index]

			# jika belum ada pasangannya maka tambahkan ke dict (value: index)
			value_index_dict[element] = index
	
	def main(self):
		print(self.twoSum([2,7,11,15], 9))
		print(self.twoSum([3,2,4], 6))
		print(self.twoSum([3,3], 6))
    
s = Solution()
s.main()

"""
Runtime: 60 ms, faster than 76.68% of Python3 online submissions for Two Sum.
Memory Usage: 15.4 MB, less than 40.97% of Python3 online submissions for Two Sum.
"""