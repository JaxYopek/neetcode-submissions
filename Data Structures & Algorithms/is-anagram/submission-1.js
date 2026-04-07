class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const str1 = s.split("").sort().join();
        const str2 = t.split("").sort().join();
        return str1 === str2
    }
}
