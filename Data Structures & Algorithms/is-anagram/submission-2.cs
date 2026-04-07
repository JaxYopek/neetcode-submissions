public class Solution {
    public bool IsAnagram(string s, string t) {
        var str1 = string.Concat(s.OrderBy(c => c));
        var str2 = string.Concat(t.OrderBy(c=>c));
        return str1 == str2;
    }
}
