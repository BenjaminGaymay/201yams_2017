#!/usr/bin/env python3

""" Birnomial function """

import math

def calc_combination(k, n):
    """ Calculs combination C """
    return float(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))


def binomial(k, n, p):
    """ Calculs binomial law """

    combination = calc_combination(k, n)
    return combination * (p**k) * (1 - p)**(n - k)
