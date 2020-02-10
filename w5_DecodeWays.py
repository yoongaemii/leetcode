'''
Decode Ways
https://leetcode.com/problems/decode-ways/
#String #Dynamic_Programming

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

'''

import math
import functools


def numDecodings(s):
    '''
    한 자리씩 돌면서 두자리수로 해석할 수 있는 가능성이 끊기는 지점을 탐색한다. 
    dp에 연속해서 두자리수로 해석할 수 있는 쌍의 개수 + 1 (=string의 길이)를 저장한다.
    각 연속개수에 대해 combination을 통해 단순 계산한 뒤 이를 곱해준다.
    Runtime: 52 ms, faster than 6.92% of Python3 online submissions for Decode Ways.
    Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Decode Ways.
    '''
    if s[0] == "0": # 0으로 시작하는 경우
        return 0

    dp = [1] # 연속가능한 게 몇 쌍나 연속으로 나오는지 '개수'를 저장한다. 원래 인덱스를 저장하려했는데 0 때문에 안될듯
    
    for i in range(len(s)-1): # i와 i+1 확인
        if s[i+1] == "0":
            if s[i] in "12": # 붙여서 디코딩하기
                dp[-1] -= 1 # 그 전 가능성 차단. 0이 두번째에 나오면 dp에 0이 들어가는 경우 고려하기
                dp.append(1) # 앞자리 수 떼어두기
                dp.append(1) # 0 떼어두기: 어차피 곱하기 1이기 때문에 괜춘
            else:
                return 0
        elif s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"): # 다음 것과 연속 가능
            dp[-1] += 1
        else:
            dp.append(1)

    result = list(map(lambda n: sum([combination(n, i) for i in range(n//2+1)]), dp))
    product = functools.reduce((lambda x, y: x * y), result)
    return product

def combination(n, i):
    '''
    the number of possible combinations where 2-digit occurs i times in an n-digit string
    '''
    ans = math.factorial(n-i) / (math.factorial(i) * math.factorial(n-2*i))
    return int(ans)

s="2263221"
print(numDecodings(s))



        
