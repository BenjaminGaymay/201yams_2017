#!/usr/bin/env python3
""" Combinaison functions """

from binomial import binomial, calc_combination


def print_result(combinaison, number, chances):
    """ Print chances """

    print("chances to get a %s %s:\t%.2f%%" % (number, combinaison, chances))


def pair(combinaison, dices):
    """ Pair combinaison. """

    not_comb = 2 - dices.count(combinaison[1])
    if not_comb > 0:
        comb = len(dices) - dices.count(combinaison[1])
        number = (binomial(not_comb, comb, 1 / 6) + binomial(comb, comb, 1 / 6)) * 100
    else:
        number = float(100)

    print_result("pair", combinaison[1], number)
    return 0


def three(combinaison, dices):
    """ Three combinaison. """

    not_comb = 3 - dices.count(combinaison[1])
    if not_comb > 0:
        comb = len(dices) - dices.count(combinaison[1])
        number = (binomial(not_comb, comb, 1 / 6) + binomial(comb, comb, 1 / 6)) * 100
    else:
        number = float(100)

    print_result("three-of-a-kind", combinaison[1], number)
    return 0


def four(combinaison, dices):
    """ Four combinaison. """

    not_comb = 4 - dices.count(combinaison[1])
    if not_comb > 0:
        comb = len(dices) - dices.count(combinaison[1])
        number = (binomial(not_comb, comb, 1/6) + binomial(comb, comb, 1/6)) * 100
    else:
        number = float(100)

    print_result("four-of-a-kind", combinaison[1], number)
    return 0


def full(combinaison, dices):
    """ Full combinaison. """

    if len(combinaison) != 3:
        return 84
    brelan, double = combinaison[1], combinaison[2]
    b_val, d_val = dices.count(brelan), dices.count(double)
    missing_b = 0 if b_val > 2 else 3 - b_val
    missing_d = 0 if d_val > 1 else 2 - d_val
    number = (calc_combination(missing_b, missing_b + missing_d) * 1/6**(missing_b + missing_d)) * 100
    print_result("full of %s" % combinaison[2], combinaison[1], number)
    return 0


def straight(combinaison, dices):
    """ Straight combinaison. """

    number = float(1)
    dices.sort()
    print_result("straight", combinaison[1], number)
    return 0


def yams(combinaison, dices):
    """ Yams combinaison. """

    comb = len(dices) - dices.count(combinaison[1])
    number = (binomial(comb, comb, 1 / 6)) * 100
    print_result("yams", combinaison[1], number)
    return 0
