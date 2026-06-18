func sortColors(nums []int) {
    l_bound, r_bound := 0, len(nums)-1
    i := 0
    for i <= r_bound {
        if nums[i] == 1 {
            i++
        } else if nums[i] == 0 {
            nums[l_bound], nums[i] = nums[i], nums[l_bound] // swap
            l_bound++
            i++
        } else if nums[i] == 2 {
            nums[r_bound], nums[i] = nums[i], nums[r_bound] // swap
            r_bound--
        }
    }
}
