// import "sort"

func mySort(word string) string {
    chars := []byte(word)
    sort.Slice(chars, func(i, j int) bool {
        return chars[i] < chars[j]
    })
    return string(chars)
}

func groupAnagrams(strs []string) [][]string {
    mappings := make(map[string][]string)
    for _, word := range strs {
        sortedWord := mySort(word)
        mappings[sortedWord] = append(mappings[sortedWord], word)
    }
    res := [][]string{}
    for _, words := range mappings {
        res = append(res, words)
    }
    return res
}
