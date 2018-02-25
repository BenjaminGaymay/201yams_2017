#!/usr/bin/env python3
""" Combinaison functions """

from binomial import binomial, calc_combination
from math import factorial
from sys import stderr

def print_result(combinaison, number, chances):
    """ Print chances """

    print("chances to get a %s %s:\t%.2f%%" % (number, combinaison, chances))


def calc_probabilities(nb_success, nb_dices, already_ok):
    """ Calculate pair, three and four probabilities """

    if nb_success > 0:
        nb_throw = nb_dices - already_ok
        number = float(0)
        while nb_success <= nb_throw:
            number += binomial(nb_success, nb_throw, 1 / 6)
            nb_success += 1
    else:
        number = float(1)
    return number


def pair(combinaison, dices):
    """ Pair combinaison. """

    if len(combinaison) > 2:
        print("Error: Too many numbers")
        return 84
    nb_success = 2 - dices.count(combinaison[1])
    number = calc_probabilities(nb_success, len(dices), dices.count(combinaison[1]))

    print_result("pair", combinaison[1], number * 100)
    return 0


def three(combinaison, dices):
    """ Three combinaison. """

    if len(combinaison) > 2:
        print("Error: Too many numbers")
        return 84
    nb_success = 3 - dices.count(combinaison[1])
    number = calc_probabilities(nb_success, len(dices), dices.count(combinaison[1]))

    print_result("three-of-a-kind", combinaison[1], number * 100)
    return 0


def four(combinaison, dices):
    """ Four combinaison. """

    if len(combinaison) > 2:
        print("Error: Too many numbers")
        return 84
    nb_success = 4 - dices.count(combinaison[1])
    number = calc_probabilities(nb_success, len(dices), dices.count(combinaison[1]))

    print_result("four-of-a-kind", combinaison[1], number * 100)
    return 0


def full(combinaison, dices):
    """ Full combinaison. """

    number = float(1)
    if len(combinaison) != 3:
        print("Error: Full: too many numbers", file=stderr)
        return 84
    if (combinaison[1] is combinaison[2]):
        print("Error: bad full combinaison")
        return 84
    if (combinaison[1] > "6" or combinaison[1] < "1" or combinaison[2] > "6" or combinaison[2] < "1"):
        print("Error: Full: number between 1 and 6", file=stderr)
        return 84
    brelan, double = combinaison[1], combinaison[2]
    b_val, d_val = dices.count(brelan), dices.count(double)
    missing_b = 0 if b_val > 2 else 3 - b_val
    missing_d = 0 if d_val > 1 else 2 - d_val
    number = (calc_combination(missing_b, missing_b + missing_d) * 1/6**(missing_b + missing_d))*100
    print_result("full of %s" % combinaison[2], combinaison[1], number)
    return 0


def straight(combinaison, dices):
    """ Straight combinaison. """

    if len(combinaison) > 2:
        print("Error: Too many numbers")
        return 84
    if combinaison[1] not in ["5", "6"]:
        print("Error: ----------", file=stderr)
        return 84
    nb_doubles = dices.count("0")
    dices = [value for value in dices if value != "0"]
    doubles = dict([(value, dices.count(value)) for value in dices])

    for double in doubles.values():
        nb_doubles += double - 1

    if combinaison[1] == "5" and "6" in doubles.keys():
        nb_doubles += 1
    elif combinaison[1] == "6" and "1" in doubles.keys():
        nb_doubles += 1

    number = factorial(nb_doubles) / 6 **nb_doubles * 100
    print_result("straight", combinaison[1], number)
    return 0


def yams(combinaison, dices):
    """ Yams combinaison. """

    if len(combinaison) > 2:
        print("Error: Too many numbers")
        return 84
    nb_throw = len(dices) - dices.count(combinaison[1])
    number = (binomial(nb_throw, nb_throw, 1 / 6)) * 100
    print_result("yams", combinaison[1], number)
    return 0
