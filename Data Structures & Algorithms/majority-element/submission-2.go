func majorityElement(nums []int) int {
    counter := 1
    curr := nums[0]
    for i := 1; i < len(nums); i++ {
        num := nums[i]
        if num != curr {
            counter--
            if counter == 0 {
                counter = 1
                curr = nums[i]
            }
        } else {
            counter++
        }
    }
    return curr
}
