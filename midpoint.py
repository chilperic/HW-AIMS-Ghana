#!/usr/bin/env python3

def integrate(f, rangex):
    riemann_sum = 0
    for i in range(len(rangex)- 1 ):
        riemann_sum += f((rangex[i + 1] - rangex[1])/2) * (rangex[i + 1] - rangex[1])
    return riemann_sum