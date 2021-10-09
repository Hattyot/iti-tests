import sys

import anti_cheat

anti_cheat.no_exception_traceback()
anti_cheat.ban_some_imports()
anti_cheat.take_down_network()
anti_cheat.no_closure()


import wat as sol  # TODO: folder
import datetime
import hashlib
import os
import random
import pytest
from _pytest.outcomes import Failed


def find_primes(n):
    primes = []
    to_check = 2
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if to_check % prime == 0:
                is_prime = False
                break
        if not is_prime:
            to_check += 1
            continue
        primes.append(to_check)
        to_check += 1
    return primes


def fibonacci(n):
    a = 1
    b = 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b


uniid = os.environ.get("uniid", "test").strip("'").lower()
hashed = int(hashlib.md5(uniid.encode('utf8')).hexdigest(), 16)
primes = find_primes(100)

funcs = {
    "a": (1, lambda a: lambda x: a),
    "b": (2, lambda a, b: lambda x: b * x + a),
    "c": (3, lambda a, b, c: lambda x: b * x ** 2 + a * x + c),
    "d": (4, lambda a, b, c, d: lambda x: b * x ** 3 + c * x ** 2 + d * x + a),
    "e": (2, lambda a, b: lambda x: (b + 1) ** (a + 1) // x),
    "f": (2, lambda a, b: lambda x: (a + b + x) ** (x // 100 + 1)),
    "g": (2, lambda a, b: lambda x: (b + 1) ** (a + 1) % x),
    "h": (2, lambda a, b: lambda x: sum(find_primes(x)) * find_primes((a * b) // 2)[-1]),
    "i": (1, lambda a: lambda x: (fibonacci(x) * fibonacci(x % (a * 5))) % x ** 2),
    "j": (1, lambda a: lambda x: int(datetime.datetime.now().strftime("%s")) % ((a // 2) + 1))
}

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

param_list = []

param_counter = 5
feedback = []
upper_lim = 2000


def get_params(n):
    global param_counter
    params = []
    for _ in range(n):
        params.append(hashed % primes[param_counter])
        param_counter += 1
    return params


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("prefirst")
@pytest.mark.weight(1)
def test_a():
    key = "a"
    params = get_params(funcs[key][0])
    param_list.append(params)
    # print(params)
    correct_func = funcs[key][1](*params)
    x = random.randint(1, upper_lim)
    actual = sol.function_a(x)
    expected = correct_func(x)
    assert type(actual) == type(1)
    if actual != expected:
        raise Failed(f"function_{key}({x}): Expected {expected}, got {actual}. TRY AGAIN!")


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("prefirst")
@pytest.mark.weight(1)
def test_b():
    key = "b"
    params = get_params(funcs[key][0])
    param_list.append(params)
    # print(params)
    correct_func = funcs[key][1](*params)
    x = random.randint(1, upper_lim)
    actual = sol.function_b(x)
    expected = correct_func(x)
    assert type(actual) == type(1)
    if actual != expected:
        raise Failed(f"function_{key}({x}): Expected {expected}, got {actual}. TRY AGAIN!")


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("prefirst")
@pytest.mark.weight(1)
def test_c():
    key = "c"
    params = get_params(funcs[key][0])
    param_list.append(params)
    # print(params)
    correct_func = funcs[key][1](*params)
    x = random.randint(1, upper_lim)
    actual = sol.function_c(x)
    expected = correct_func(x)
    assert type(actual) == type(1)
    if actual != expected:
        raise Failed(f"function_{key}({x}): Expected {expected}, got {actual}. TRY AGAIN!")


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("prefirst")
@pytest.mark.weight(1)
def test_d():
    key = "d"
    params = get_params(funcs[key][0])
    param_list.append(params)
    # print(params)
    correct_func = funcs[key][1](*params)
    x = random.randint(1, upper_lim)
    actual = sol.function_d(x)
    expected = correct_func(x)
    assert type(actual) == type(1)
    if actual != expected:
        raise Failed(f"function_{key}({x}): Expected {expected}, got {actual}. TRY AGAIN!")


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("prefirst")
@pytest.mark.weight(1)
def test_e():
    key = "e"
    params = get_params(funcs[key][0])
    param_list.append(params)
    # print(params)
    correct_func = funcs[key][1](*params)
    x = random.randint(1, upper_lim)
    actual = sol.function_e(x)
    expected = correct_func(x)
    assert type(actual) == type(1)
    if actual != expected:
        raise Failed(f"function_{key}({x}): Expected {expected}, got {actual}. TRY AGAIN!")


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("prefirst")
@pytest.mark.weight(1)
def test_f():
    key = "f"
    params = get_params(funcs[key][0])
    param_list.append(params)
    # print(params)
    correct_func = funcs[key][1](*params)
    x = random.randint(1, upper_lim)
    actual = sol.function_f(x)
    expected = correct_func(x)
    assert type(actual) == type(1)
    if actual != expected:
        raise Failed(f"function_{key}({x}): Expected {expected}, got {actual}. TRY AGAIN!")


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("prefirst")
@pytest.mark.weight(1)
def test_g():
    key = "g"
    params = get_params(funcs[key][0])
    param_list.append(params)
    # print(params)
    correct_func = funcs[key][1](*params)
    x = random.randint(1, upper_lim)
    actual = sol.function_g(x)
    expected = correct_func(x)
    assert type(actual) == type(1)
    if actual != expected:
        raise Failed(f"function_{key}({x}): Expected {expected}, got {actual}. TRY AGAIN!")


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("prefirst")
@pytest.mark.weight(1)
def test_h():
    key = "h"
    params = get_params(funcs[key][0])
    param_list.append(params)
    # print(params)
    correct_func = funcs[key][1](*params)
    x = random.randint(1, upper_lim)
    actual = sol.function_h(x)
    expected = correct_func(x)
    assert type(actual) == type(1)
    if actual != expected:
        raise Failed(f"function_{key}({x}): Expected {expected}, got {actual}. TRY AGAIN!")


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("prefirst")
@pytest.mark.weight(1)
def test_i():
    key = "i"
    params = get_params(funcs[key][0])
    param_list.append(params)
    # print(params)
    correct_func = funcs[key][1](*params)
    x = random.randint(1, upper_lim)
    actual = sol.function_i(x)
    expected = correct_func(x)
    assert type(actual) == type(1)
    if actual != expected:
        raise Failed(f"function_{key}({x}): Expected {expected}, got {actual}. TRY AGAIN!")


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("prefirst")
@pytest.mark.weight(1)
def test_j():
    key = "j"
    params = get_params(funcs[key][0])
    param_list.append(params)
    # print(params)
    correct_func = funcs[key][1](*params)
    x = random.randint(1, upper_lim)
    actual = sol.function_j(x)
    expected = correct_func(x)
    assert type(actual) == type(1)
    if actual != expected:
        raise Failed(f"function_{key}({x}): Expected {expected}, got {actual}. TRY AGAIN!")


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("prefirst")
@pytest.mark.weight(1)
def test_sum():
    global param_counter
    param_counter = 10
    a, b = get_params(2)
    a = a % 10
    b = b % 10
    # print([a, b])
    x = random.randint(1, upper_lim)
    first_side = funcs[letters[a]][1](*param_list[a])
    second_side = funcs[letters[b]][1](*param_list[b])
    expected = first_side(x) + second_side(x)
    actual = sol.function_sum(x)
    assert type(actual) == type(1)
    if actual != expected:
        raise Failed(f"function_sum({x}): Expected {expected}, got {actual}. TRY AGAIN!")


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("prefirst")
@pytest.mark.weight(1)
def test_multiple():
    global param_counter
    param_counter = 12
    a, b = get_params(2)
    a = a % 10
    b = b % 10
    # print([a, b])
    x = random.randint(1, upper_lim)
    first_side = funcs[letters[a]][1](*param_list[a])
    second_side = funcs[letters[b]][1](*param_list[b])
    expected = first_side(x) * second_side(x)
    actual = sol.function_multiple(x)
    assert type(actual) == type(1)
    if actual != expected:
        raise Failed(f"function_multiple({x}): Expected {expected}, got {actual}. TRY AGAIN!")


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("prefirst")
@pytest.mark.weight(1)
def test_mod():
    global param_counter
    param_counter = 14
    a, b = get_params(2)
    a = a % 10
    b = b % 10
    # print([a, b])
    x = random.randint(1, upper_lim)
    first_side = funcs[letters[a]][1](*param_list[a])
    second_side = funcs[letters[b]][1](*param_list[b])
    expected = first_side(x) % second_side(x)
    actual = sol.function_mod(x)
    assert type(actual) == type(1)
    if actual != expected:
        raise Failed(f"function_mod({x}): Expected {expected}, got {actual}. TRY AGAIN!")


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("prefirst")
@pytest.mark.weight(1)
def test_composition():
    global param_counter
    param_counter = 16
    a, b = get_params(2)
    a = a % 10
    b = b % 10
    # print([a, b])
    x = random.randint(1, upper_lim)
    first_side = funcs[letters[a]][1](*param_list[a])
    second_side = funcs[letters[b]][1](*param_list[b])
    expected = first_side(second_side(x) % upper_lim)
    actual = sol.function_composition(x)
    assert type(actual) == type(1)
    if actual != expected:
        raise Failed(f"function_composition({x}): Expected {expected}, got {actual}. TRY AGAIN!")


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("prefirst")
@pytest.mark.weight(1)
def test_meta_composition():
    global param_counter
    param_counter = 18
    a = get_params(1)[0]
    a = a % 10
    # print([a])
    x = random.randint(1, upper_lim)
    first_side = funcs[letters[a]][1](*param_list[a])
    first_value = first_side(x) % 10
    second_side = funcs[letters[first_value]][1](*param_list[first_value])
    expected = second_side(x)
    actual = sol.function_meta_composition(x)
    assert type(actual) == type(1)
    if actual != expected:
        raise Failed(f"function_meta_composition({x}): Expected {expected}, got {actual}. TRY AGAIN!")
