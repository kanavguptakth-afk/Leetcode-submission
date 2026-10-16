class Solution:
    def characterReplacement(self, s, k):
        count={}
        left=maximum=max_freq=0

        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            max_freq=max(max_freq,count[s[right]])

            while(right-left+1)-max_freq>k:
                count[s[left]]-=1
                left+=1

            maximum=max(maximum,right-left+1)

        return maximum            
        