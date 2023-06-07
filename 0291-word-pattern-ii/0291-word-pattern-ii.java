import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public boolean wordPatternMatch(String pattern, String s) {
        Map<Character, String> mapping = new HashMap<>();
        Set<String> mapped = new HashSet<>();

        boolean result = helper(0, 0, pattern, s, mapping, mapped);
        
        return result;
    }

    private boolean helper(int i, int j, String pattern, String s, Map<Character, String> mapping, Set<String> mapped) {
        if (i == pattern.length() && j == s.length()) {
            return true;
        }

        if (i >= pattern.length() || j >= s.length()) {
            return false;
        }

        if (!mapping.containsKey(pattern.charAt(i))) {
            for (int length = 1; length <= s.length() - j; length++) {
                String substring = s.substring(j, j + length);
                if (!mapped.contains(substring)) {
                    mapped.add(substring);
                    mapping.put(pattern.charAt(i), substring);
                    if (helper(i + 1, j + length, pattern, s, mapping, mapped)) {
                        return true;
                    }
                    mapping.remove(pattern.charAt(i));
                    mapped.remove(substring);
                }
            }
        } else {
            String mappedString = mapping.get(pattern.charAt(i));
            if (s.startsWith(mappedString, j) && helper(i + 1, j + mappedString.length(), pattern, s, mapping, mapped)) {
                return true;
            }
        }

        return false;
    }
}
