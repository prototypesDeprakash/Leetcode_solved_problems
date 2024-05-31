'''
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
'''
s = "babad"
for i in range(0,len(s)):
    for j in range(i,len(s)):
        print(s[j],end="")
    print()