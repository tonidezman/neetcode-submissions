type Solution struct{}

func (s *Solution) Encode(strs []string) string {
    res := []string{}
    for _, word := range strs {
        res = append(res, fmt.Sprintf("%d#%s", len(word), word))
    }
    return strings.Join(res, "")
}

func isDigit(s string) bool {
    if s[0] < '0' || s[0] > '9' {
        return false
    }
    return true
}

func (s *Solution) Decode(encoded string) []string {
    res := []string{}
    i := 0
    for i < len(encoded) {
        curr := []string{}
        for isDigit(string(encoded[i])) && encoded[i] != '#' {
            curr = append(curr, string(encoded[i]))
            i++
        }
        i++
        numStr := strings.Join(curr, "")
        num, _ := strconv.ParseInt(numStr, 10, 64)
        res = append(res, encoded[i:i+int(num)])
        i += int(num)
    }
    return res
}
