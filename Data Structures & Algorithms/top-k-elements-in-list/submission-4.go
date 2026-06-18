func topKFrequent(nums []int, k int) []int {
    // count the numbers
    counter := make(map[int]int)
    for _, num := range nums {
        if _, exists := counter[num]; !exists {
            counter[num] = 0
        }
        counter[num]++
    }
    bucket := make([][]int, len(nums)+1)
    for num, count := range counter {
        bucket[count] = append(bucket[count], num)
    }
    res := []int{}
    for i := len(bucket)-1; i>0; i-- {
        for _, num := range bucket[i] {
            if k == 0 {
                return res
            }
            res = append(res, num)
            k--
        }
    }
    return res
}
