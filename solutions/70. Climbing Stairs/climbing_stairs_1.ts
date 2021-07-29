function climbStairsRec(n: number, memo: number[]): number {
  if (n == 0) return 0 // []
  if (n == 1) return 1 // [1]
  if (n == 2) return 2 // [1,1] [2]
  if (memo[n] != null) return memo[n]
  else memo[n] = climbStairsRec(n - 1, memo) + climbStairsRec(n - 2, memo)
  // Kita hitung kalau misal saat ini kita ambil 1 langkah maka sisanya berapa, demikian dengan yang 2 langkah
  return memo[n]
};

function climbStairs(n: number) : number {
  return climbStairsRec(n, [])
}
console.log(climbStairs(0))
console.log(climbStairs(1))
console.log(climbStairs(2))
console.log(climbStairs(3))

/**
 * climbStairs(1) = 1
 * climbStairs(2) = [2], [1,1] = 2
 * climbStairs(3) = [1,1,1] [1,2] [2,1]
 * Recursion: cari base case
 * Memoizazion: save the value
 * Basically a fibbonacci problem
 */

/**
 * Runtime: 72 ms, faster than 90.44% of TypeScript online submissions for Climbing Stairs.
 * Memory Usage: 40.4 MB, less than 40.61% of TypeScript online submissions for Climbing Stairs.
 */