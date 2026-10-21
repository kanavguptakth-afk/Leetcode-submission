class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def judge(x, y):
            for i in range(52):
                if x[i] < y[i]:
                    return False
            return True

        cnt = [0] * 52

        def to_index(c):
            if ord("A") <= ord(c) <= ord("Z"):
                return ord(c) - ord("A")
            elif ord("a") <= ord(c) <= ord("z"):
                return ord(c) - ord("a") + 26
            else:
                return None

        target = [0] * 52
        for i in range(len(t)):
            target[to_index(t[i])] += 1

        ans = ""
        ans_length = float("inf")
        l = 0
        for r in range(len(s)):
            cnt[to_index(s[r])] += 1
            if judge(cnt, target):
                while l < r:
                    cnt[to_index(s[l])] -= 1
                    if judge(cnt, target):
                        l += 1
                    else:
                        cnt[to_index(s[l])] += 1
                        break

                if ans_length > r - l + 1:
                    ans_length = r - l + 1
                    ans = s[l:r+1]
        
        return ans