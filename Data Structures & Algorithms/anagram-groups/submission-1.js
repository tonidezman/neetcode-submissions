class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let anagrams = {}
        for (let s of strs) {
            let key = s.split('').sort().join('')
            if (key in anagrams) {
                anagrams[key].push(s)
            } else {
                anagrams[key] = [s]
            }
        }
        return Object.values(anagrams)
    }
}
