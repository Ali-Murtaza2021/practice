def solution(x, y):
    return str(int((((x+y-1)*(x+y-2))/2) + x))

print(solution(1, 1))
print(solution(2, 1))
print(solution(3, 2))
print(solution(2, 3))