'''
WorkBreak
https://leetcode.com/problems/word-break/   
#Medium #Dynamic_Programming

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''




def wordBreak(s, wordDict):
    '''
    [Time Limit Exceeded]
    startswith로 사전의 모든 단어를 갖다대보는 기본적인 recursion
    '''
    if s in wordDict:
        return True

    return any([wordBreak(s[len(w):], wordDict) for w in wordDict if s.startswith(w)]) # any([]) == False

def wordBreak(s, wordDict):
    ''' 
    https://leetcode.com/problems/word-break/discuss/43808/Simple-DP-solution-in-Python-with-description
    dp에 사전의 어느 단어가 스트링의 i 부터 j까지 발생한다는 것을 저장하려고만 생각했는데 
    1. 어느 단어에 해당하는지는 저장할 필요가 없다. 매칭이 됐다는 사실이 중요하다.
    2. 중간 매칭(i가 0이 아닌 경우)은 의미가 없다. 빠짐없이 연속적으로 매치하는 결과만을 카운트하니 앞에서부터(i고정) 어디까지가 연속적인 매치에 성공했는지만 기록하면 된다.
    Runtime: 52 ms, faster than 16.23% of Python3 online submissions for Word Break. O(NM)
    Memory Usage: 13 MB, less than 94.44% of Python3 online submissions for Word Break. 
    '''
    dp = [0] # j까지는 연속적으로 채울 수 있다는 뜻임. 여기에 len(s)가 들어와야 함
    for j in range(1,len(s)+1):
        if any(s[i:j] in wordDict for i in dp): 
            dp.append(j)
    
    return len(s) in dp

# s = "appleet"
# wordDict = ["app", "apple", "et"]

# s = "applepenapple"
# wordDict = ["apple", "pen"]

# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# 길이가 긴 것을 우선 계산?

print(wordBreak(s, wordDict))


'''
DFS 풀이법
https://leetcode.com/problems/word-break/discuss/428606/Python-Simple-Iterative-BFS-or-DFS-24ms

'''

'''
장현준님 풀이
wordDict에서 길이의 min과 max를 저장해서 확인해야하는 경우의 수를 줄였다
'''