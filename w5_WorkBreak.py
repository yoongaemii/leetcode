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
    for j in range(1,len(s)+1): # 여기에서 i를 알았다면 start+1 부터 len(s)+1까지만 검사할 수 있었음. 즉, 다음줄에서 s[2:1]과 같은 불필요한 검사를 하고 있다는 뜻. 근데 i는 항상 j보다 작아. j인적이 있었던 놈들만 들어가니까
        if any(s[i:j] in wordDict for i in dp): 
            dp.append(j)
    
    return len(s) in dp



def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    '''O(N^2)/O(N)'''
    wordDict, N, dp = set(wordDict), len(s), [True]
    for i in range(1, N + 1): 
        dp += any(dp[j] and s[j:i] in wordDict for j in range(i)), # i보다 작은 모든 j에 대하여 dp에 lookup을 해야함
    return dp[-1]


def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    '''
    O(N^2)/O(N)
    과정 상으로는 별 다를 게 없어 보이는 데 왜 더 빠를까?
    visited가 dp처럼 중복 업무를 방지하는 역할을 하고 있기 때문? start가 이미 visited이면(즉, 해당 자리까지 만들 수 있다는게 판명이 나면) 그 작업을 건너뛰니까
    visited의 결과는 for loop 풀이의 dp와 동일함. 
    여기에서 queue의 효과는 '여기까지는 만들 수 있습니다' 하고 입력하는 부분의 위계와 검사하는 부분의 위계를 분리시켜서 생각했다는 것.
    아닌가 그냥 더 빨리 종료되기 때문인가?
    '''
    wordDict, visited, queue = set(wordDict), [False] * len(s), deque([])
    queue.append(0)
    while queue:
        start = queue.popleft()
        if not visited[start]:
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordDict:
                    queue.append(end)
                    if end == len(s): return True
            visited[start] = True
    return False

s = "leetcode"
wordDict = ["leet", "code"]
wordBreak(s, wordDict)

'''
장현준님 풀이
wordDict에서 길이의 min과 max를 저장해서 확인해야하는 경우의 수를 줄였다
'''