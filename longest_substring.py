'''Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

'''

def longestSubString(s, k):
    stack = []
    res = []
    for (index, char) in enumerate(s):
        stack.append(char)

        for c in s[index+1:]:
            stack.append(c)
            if len(set(stack)) == k:
                res.append(''.join(stack))
            elif len(set(stack)) > k:
                stack = []
                break
        stack = []

    return max(res, key=len)

# assert longestSubString("abcba",2) == "bcb"
# assert longestSubString("abcba",3) == "abcba"
assert longestSubString("aabbcc",1) == ["aa" ,"bb", "cc"]