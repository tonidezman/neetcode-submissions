func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)
    for idx, num := range nums {
        otherNum := target - num
        if i, exists := seen[otherNum]; exists {
            return []int{i, idx}
        }
        seen[num] = idx
    }
    return []int{-1, -1}
}
