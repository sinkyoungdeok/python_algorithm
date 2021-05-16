"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12936
문제 접근 방법: 조합 
"""
from itertools import permutations

def solution(n, k):
    temp = []
    for i in range(1, n+1):
        temp.append(i)
    
    per = permutations(temp)
    for i,p in enumerate(per):
        if i+1 == k:
            return list(p)


n = 3
k = 5
print(solution(n,k))