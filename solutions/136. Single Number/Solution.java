class Solution {
  public static void main(String[] args) {
    Solution s = new Solution();
    System.out.println(s.singleNumber(new int[] { 1, 2, 3, 3, 1 }));
  }

  public int singleNumber(int[] nums) {
    int singleNumber = nums[0];
    for (int i = 1; i < nums.length; i++) {
      singleNumber = singleNumber ^ nums[i];
    }
    return singleNumber;
  }
  /**
   * Ide: [1,2,3,3,1] [001,010,011,011,001] pake XOR x xor x = 0 dan xor
   * komutatif, artinya a xor b = b xor a misal ada 3 angka 1,2,1 1 xor 2 xor 1 =
   * 1 xor 1 xor 2 = 0 xor 2 = 2
   */

  /**
   * Runtime: 1 ms, faster than 94.80% of Java online submissions for Single
   * Number. Memory Usage: 39.4 MB, less than 50.28% of Java online submissions
   * for Single Number.
   */
}