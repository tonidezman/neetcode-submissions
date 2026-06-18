func merge(left []int, right []int) []int {
    l, r := 0, 0
    res := []int{}
    for l < len(left) && r < len(right) {
        if left[l] < right[r] {
            res = append(res, left[l])
            l++
        } else {
            res = append(res, right[r])
            r++
        }
    }
    for l < len(left) {
        res = append(res, left[l])
        l++
    }
    for r < len(right) {
        res = append(res, right[r])
        r++
    }
    return res
}

func sortArray(nums []int) []int {
    if len(nums) < 2 {
        return nums
    }
    mid := len(nums) / 2
    left := sortArray(nums[:mid])
    right := sortArray(nums[mid:])
    return merge(left, right)
}
