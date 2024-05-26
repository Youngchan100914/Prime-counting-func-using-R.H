N = int(input())
s = input()
def solution(s_2=s, cnt = 0):
    x = len(s_2)
    if '()' not in s_2.replace('()', ''):
        return int(cnt+(x-len(s_2.replace('()', '')))/2+len(s_2.replace('()', '')))
    return solution(s_2.replace('()', ''), int(cnt+(x-len(s_2.replace('()', '')))/2))
print(solution())