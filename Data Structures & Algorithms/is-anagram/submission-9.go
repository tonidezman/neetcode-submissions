func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }
    counter := make(map[rune]int)
    for _, c := range s {
        if _, exists := counter[c]; !exists {
            counter[c] = 0
        } 
        counter[c]++
    }

    for _, c := range t {
        if _, exists := counter[c]; !exists {
            return false
        } else {
            counter[c]--
        }
    }
    for _, count := range counter {
        if count != 0 {
            return false
        }
    }
    return true
}
