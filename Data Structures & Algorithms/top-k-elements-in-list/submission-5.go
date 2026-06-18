func myCounter(nums []int) map[int]int {
    counter := make(map[int]int)
    for _, num := range nums {
        if _, exists := counter[num]; !exists {
            counter[num] = 0
        }
        counter[num]++
    }
    return counter
}

func bucketSort(counter map[int]int, n int) [][]int {
    res := make([][]int, n+1)
    for num, count := range counter {
        res[count] = append(res[count], num)
    }
    return res
}

func topKFrequent(nums []int, k int) []int {
    counter := myCounter(nums) // helper
    bucket := bucketSort(counter, len(nums)) // helper
    res := make([]int, 0)
    for i := len(bucket)-1; i >= 0; i-- {
        for _, num := range bucket[i] {
            res = append(res, num)
            k--
            if k == 0 {
                return res
            }
        }
    }
    return res
}