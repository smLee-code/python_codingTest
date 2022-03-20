import sys
input = sys.stdin.readline

data = list(map(int, input().split()))
data.sort()

for n in data:
    print(n, end=' ')
print()