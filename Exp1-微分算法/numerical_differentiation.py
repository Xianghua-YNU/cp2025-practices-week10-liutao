import numpy as np
import matplotlib.pyplot as plt
from sympy import tanh, symbols, diff, lambdify

def f(x):
    """计算函数值 f(x) = 1 + 0.5*tanh(2x)"""
    return 1 + 0.5 * np.tanh(2 * x)

def get_analytical_derivative():
    """使用sympy获取解析导数函数"""
    x = symbols('x')
    expr = 1 + 0.5 * tanh(2 * x)
    df_expr = diff(expr, x)
    return lambdify(x, df_expr, 'numpy')

def calculate_central_difference(x, f):
    """使用中心差分法计算数值导数"""
    h = x[1] - x[0]
    f_x = f(x)
    dy = (f_x[2:] - f_x[:-2]) / (2 * h)
    return dy

def richardson_derivative_all_orders(x, f, h, max_order=3):
    """使用Richardson外推法计算不同阶数的导数值"""
    D = []
    for i in range(max_order + 1):
        h_i = h / (2 ** i)
        d = (f(x + h_i) - f(x - h_i)) / (2 * h_i)
        current_row = [d]
        for m in range(1, i + 1):
            prev_d = current_row[m-1]
            prev_prev_d = D[i-1][m-1]
            factor = (4 ** m) - 1
            extrapolated = prev_d + (prev_d - prev_prev_d) / factor
            current_row.append(extrapolated)
        D.append(current_row)
    results = [D[m][m] for m in range(max_order + 1)]
    return results

def create_comparison_plot(x, x_central, dy_central, dy_richardson, df_analytical):
    """创建对比图，展示导数计算结果和误差分析"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 12))
    
    # 导数对比图
    ax1.plot(x_central, dy_central, label='Central Difference')
    ax1.plot(x_central, dy_richardson, label='Richardson')
    ax1.plot(x_central, df_analytical(x_central), label='Analytical', linestyle='--')
    ax1.legend()
    ax1.set_title('Derivative Comparison')
    
    # 误差分析图（对数坐标）
    error_central = np.abs(dy_central - df_analytical(x_central))
    error_richardson = np.abs(dy_richardson - df_analytical(x_central))
    ax2.semilogy(x_central, error_central, label='Central Error')
    ax2.semilogy(x_central, error_richardson, label='Richardson Error')
    ax2.legend()
    ax2.set_title('Error Analysis (log scale)')
    
    # Richardson外推不同阶数误差对比图
    x_val = x_central[len(x_central)//2]
    h_initial = x[1] - x[0]
    max_order = 3
    richardson_results = richardson_derivative_all_orders(x_val, f, h_initial, max_order)
    true_deriv = df_analytical(x_val)
    orders = list(range(max_order + 1))
    errors = [np.abs(r - true_deriv) for r in richardson_results]
    ax3.semilogy(orders, errors, 'o-')
    ax3.set_xticks(orders)
    ax3.set_xlabel('Richardson Order')
    ax3.set_ylabel('Error (log scale)')
    ax3.set_title('Richardson Error by Order')
    
    # 步长敏感性分析图（双对数坐标）
    h_values = np.logspace(-5, 0, 10)
    central_errors = []
    richardson_errors = []
    for h in h_values:
        central_est = (f(x_val + h) - f(x_val - h)) / (2 * h)
        central_errors.append(np.abs(central_est - true_deriv))
        richardson_est = richardson_derivative_all_orders(x_val, f, h, 3)[-1]
        richardson_errors.append(np.abs(richardson_est - true_deriv))
    ax4.loglog(h_values, central_errors, 'o-', label='Central')
    ax4.loglog(h_values, richardson_errors, 's-', label='Richardson')
    ax4.set_xlabel('Step Size (h)')
    ax4.set_ylabel('Error')
    ax4.legend()
    ax4.set_title('Step Size Sensitivity')
    
    plt.tight_layout()
    plt.show()

def main():
    """运行数值微分实验的主函数"""
    x = np.linspace(-2, 2, 1000)
    h_initial = x[1] - x[0]
    df_analytical = get_analytical_derivative()
    dy_central = calculate_central_difference(x, f)
    x_central = x[1:-1]
    
    # 计算Richardson外推（最高阶结果）
    dy_richardson = []
    for xi in x_central:
        results = richardson_derivative_all_orders(xi, f, h_initial, 3)
        dy_richardson.append(results[-1])
    dy_richardson = np.array(dy_richardson)
    
    create_comparison_plot(x, x_central, dy_central, dy_richardson, df_analytical)

if __name__ == '__main__':
    main()
