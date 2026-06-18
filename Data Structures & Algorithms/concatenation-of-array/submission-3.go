func getConcatenation(nums []int) []int {
    ans := []int{}
    n := len(nums)
    for i := 0; i < n*2; i++ {
        ans = append(ans, nums[i%n])
    }
    return ans
}
