import numpy as np

# 待积分函数


def f(x):
    # 实现被积函数 f(x) = x^4 - 2x + 1
    return x**4 - 2*x + 1

# 梯形法则积分函数（供参考比较用）


def trapezoidal(f, a, b, N):
    """
    梯形法数值积分
    :param f: 被积函数
    :param a: 积分下限
    :param b: 积分上限
    :param N: 子区间数
    :return: 积分近似值
    """
    h = (b - a) / N
    x = np.linspace(a, b, N + 1)
    y = f(x)
    return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

# Simpson法则积分函数


def simpson(f, a, b, N):
    if N % 2 != 0:
        raise ValueError("N必须为偶数")
    h = (b - a) / N
    x = np.linspace(a, b, N + 1)
    y = f(x)
    # 拆分计算
    sum_odd = np.sum(y[1:-1:2])
    sum_even = np.sum(y[2:-2:2])
    result = (h / 3) * (y[0] + 4 * sum_odd + 2 * sum_even + y[-1])
    return result


def main():
    a, b = 0, 2  # 积分区间
    exact_integral = 4.4  # 精确解

    for N in [100, 1000]:  # 不同子区间数
        # 调用积分函数并计算误差
        trapezoidal_result = trapezoidal(f, a, b, N)
        simpson_result = simpson(f, a, b, N)

        # 计算相对误差
        trapezoidal_error = abs(trapezoidal_result -
                                exact_integral) / exact_integral
        simpson_error = abs(simpson_result - exact_integral) / exact_integral

        # 输出结果
        print(f"N = {N}")
        print(
            f"梯形法则结果: {trapezoidal_result:.8f}, 相对误差: {trapezoidal_error:.2e}")
        print(f"Simpson法则结果: {simpson_result:.8f}, 相对误差: {simpson_error:.2e}")
        print("-" * 40)


if __name__ == '__main__':
    main()
