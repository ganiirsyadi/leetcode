from typing import List


class Solution:
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
    #     nums = [0] + nums
    #     for i in range(len(nums)):
    #         index = abs(nums[i])
    #         nums[index] = -abs(nums[index])

    #     return [i for i in range(len(nums)) if nums[i] > 0]

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:        
        for i in range(len(nums)):
            index = abs(nums[i]) - 1 
            # agar ga out of range karena nilai max n tapi index max n - 1, 
            # jadi angka 3 akan diflag pada index ke-2
            nums[index] = -abs(nums[index])
        return [i for i in range(1, len(nums) + 1) if nums[i - 1] > 0]


solution = Solution()
print(solution.findDisappearedNumbers([]))
"""
tandai semua angka yang udah muncul dengan cara menandai index pada nums 
sesuai angka yang udah muncul
misal
awal: [5,2,1,2,1] 
* panjang list = value max dari list
karena index maksimum bisa = 5 dan itu out of range, maka kita bisa tambahkan 0 di awal
menjadi: [0,5,2,1,2,1]
waktu cek 0, dia akan tetep jadi nol karena -(abs(arr[abs(0)])) = 0
waktu cek 5, kita tandai index ke 5 jadi negatif
menjadi: [0,5,2,1,2,-1]
dst
final: [0,-5,-2,1,2,-1]

kenapa pake abs, karena value dari arr[index] bisa berganti-ganti antara positif-negatif
(ingat value arr tidak unik)
jika tanpa abs, misal sebelumnya [0,1,1] akan menjadi [0, -1, 1] kemudian dinegasikan akan menjadi [0,1,1]
(positif kembali)
"""

"""
Runtime: 393 ms, faster than 27.62% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 21.8 MB, less than 83.78% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""