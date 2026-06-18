func productExceptSelf(nums []int) []int {
    prev := 1
    prefix := make([]int, len(nums))
    for i := range nums {
        prefix[i] = prev
        prev = nums[i] * prev
    }
    prev = 1
    for i := len(nums)-1; i >= 0; i-- {
        prefix[i] *= prev
        curr := prev * nums[i]
        prev = curr
    }
    return prefix
}
