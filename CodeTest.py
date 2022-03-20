import sys

def rec(cnt = 5):
    if cnt >= 0:
        print(cnt)
        rec(cnt - 1)

rec()