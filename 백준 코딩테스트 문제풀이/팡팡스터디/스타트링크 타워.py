import sys
input = sys.stdin.readline


n = int(input())
board = [list(map(str, input().rstrip())) for _ in range(5)]

zero = [['#', '#', '#'], [], [], [], ['#', '#', '#']]
one = [[], [], [], [], []]
two = [['#', '#', '#'], [], ['#', '#', '#'], [], ['#', '#', '#']]
three = [['#', '#', '#'], [], ['#', '#', '#'], [], ['#', '#', '#']]
four = [[], [], ['#', '#', '#'], [], []]
five = [['#', '#', '#'], [], ['#', '#', '#'], [], ['#', '#', '#']]
six = [['#', '#', '#'], [], ['#', '#', '#'], [], ['#', '#', '#']]
seven = [['#', '#', '#'], [], [], [], []]
eight = [['#', '#', '#'], [], ['#', '#', '#'], [], ['#', '#', '#']]
nine = [['#', '#', '#'], [], ['#', '#', '#'], [], ['#', '#', '#']]

for i in range(5):
    print(board[i])