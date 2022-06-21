def backtrack(depth, visited, answer, m, n, numbers):
    if depth == m:
        for i in range(m):
            print(answer[i], end=' ')
        print()
        return
    
    for x in range(n):
        if visited[x]:
            continue
        visited[x] = True
        answer.append(numbers[x])
        backtrack(depth+1, visited, answer, m, n, numbers)
        visited[x] = False
        answer.pop()
    return

def solution():
    
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()
    visited = [False] * n
    answer = []
    backtrack(0, visited, answer, m, n, numbers)
    
solution()