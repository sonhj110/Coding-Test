# 문제링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12909

# 1트 - 테스트 케이스 통과 X
def solution(s):
    
    if s[0] == ')' or s[-1] == '(' :
        return False
    elif s.count('(') != s.count(')') :
        return False
    else :
        return True
    
# 2트 - 효율성 테스트 통과 X
def solution(s):
    
    if s[0] == ')' or s[-1] == '(' :
        return False
    elif s.count('(') != s.count(')') :
        return False
    
    else :
        for i in range(3,len(s)+1) : # 이진탐색?
            open_p = s[:i].count('(')
            close_p = s[:i].count(')')
            if close_p > open_p :
                return False
        return True
        