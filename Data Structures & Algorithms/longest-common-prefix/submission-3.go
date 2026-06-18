func longestCommonPrefix(strs []string) string {
    for i := 0; i < len(strs[0]); i++ {
        c := strs[0][i]
        for _, word := range strs {
            if i >= len(word) || c != word[i] {
                return strs[0][:i]
            }
        }
    }
    return strs[0]
}
