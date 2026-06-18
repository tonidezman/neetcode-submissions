func removeElement(nums []int, val int) int {
    left := 0
    right := 0
    for right < len(nums) {
        if nums[right] == val {
            right++
        } else {
            nums[left] = nums[right]
            left++
            right++
        }
    }
    return left
}
