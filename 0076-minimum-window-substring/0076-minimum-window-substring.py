
class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        left = 0
        have = 0
        required = len(need)
        window = {}
        result = ""
        min_len = float("inf")

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        return result
