#!/bin/python3

import sys

def productOfLegoTypes(a, b, c, d, p, q):
    num = [a, b, c, d]
    num.remove(p)
    num.remove(q)
    return num[0] * num[1]

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        a, b, c, d = input().strip().split(' ')
        a, b, c, d = [int(a), int(b), int(c), int(d)]
        p, q = input().strip().split(' ')
        p, q = [int(p), int(q)]
        answer = productOfLegoTypes(a, b, c, d, p, q)
        print(answer)
