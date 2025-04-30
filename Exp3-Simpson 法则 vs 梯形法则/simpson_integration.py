import pytest
import numpy as np

# 假设原有的simpson函数和trapezoidal函数已经定义


def simpson(f, a, b, N):
    if N % 2 != 0:
        raise ValueError("N必须为偶数")
    h = (b - a) / N
    x = np.linspace(a, b, N + 1)
    y = f(x)
    sum_odd = np.sum(y[1:-1:2])
    sum_even = np.sum(y[2:-2:2])
    result = (h / 3) * (y[0] + 4 * sum_odd + 2 * sum_even + y[-1])
    return result


def trapezoidal(f, a, b, N):
    h = (b - a) / N
    x = np.linspace(a, b, N + 1)
    y = f(x)
    return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

# 定义被积函数


def f(x):
    return x**4 - 2 * x + 1

# 测试Simpson法则


def test_simpson():
    a, b = 0, 2
    N = 100
    exact = 4.4
    result = simpson(f, a, b, N)
    error = abs(result - exact) / exact
    assert error < 0.01

# 测试梯形法则


def test_trapezoidal():
    a, b = 0, 2
    N = 100
    exact = 4.4
    result = trapezoidal(f, a, b, N)
    error = abs(result - exact) / exact
    assert error < 0.01
