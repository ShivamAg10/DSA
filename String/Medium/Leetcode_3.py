class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if s == "":
        #     return 0
        # stk = []
        # count = 0
        # curr_count = 0
        # for i in s:
        #     if i not in stk:
        #         stk.append(i)
        #         curr_count += 1
        #     elif curr_count > count:
        #         count = curr_count
        #         curr_count = 1 
        #         stk = [i]
        # if curr_count > count:
        #     count = curr_count
        # return count

        max_subString = 0
        subString = ""
        for i in range(len(s)):
            subString += s[i]
            for j in range(i+1, len(s)):
                if s[j] not in subString:
                    subString += s[j]
                else:
                    break
            if len(subString) > max_subString:
                max_subString = len(subString)
            subString = ""
        return max_subString