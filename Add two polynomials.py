def read_polynomial():
    n = int(input())
    polynomial_dict = {}
    for i in range(n):
        power, coefficient = map(int, input().split())
        polynomial_dict[power] = coefficient
    return polynomial_dict
def get_term(coefficient, power):
    coefficient = abs(coefficient)
    if coefficient == 1 and power != 0:
        coefficient = ""
    if power > 1:
        term = "{}x^{}".format(coefficient, power)
    elif power == 1:
        term = "{}x".format(coefficient)
    elif power == 0:
        term = "{}".format(coefficient)
    return term