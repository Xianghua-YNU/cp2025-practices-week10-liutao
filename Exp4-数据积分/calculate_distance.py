import numpy as np
from scipy.integrate import cumulative_trapezoid
import matplotlib.pyplot as plt
import os

def main():
    try:
        # 1. 获取数据文件路径（TODO：使用相对路径）
        print("[调试] 当前工作目录:", os.getcwd())
        data_file = 'Velocities.txt'
        print("[调试] 尝试读取的完整路径:", os.path.abspath(file_path))

        # 检查文件是否存在
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"错误：文件 {os.path.abspath(file_path)} 不存在！")
        # 2. 读取数据（TODO：使用numpy.loadtxt）
        try:
            data = np.loadtxt(file_path)
        except Exception as e:
            print(f"读取文件失败: {e}")
            exit()

        t = data[:, 0]  # 时间列
        v = data[:, 1]  # 速度列

        # 3. 计算总距离（TODO：使用numpy.trapz）
        total_distance = np.trapz(v, t)
        print(f"总运行距离: {total_distance:.2f} 米")

        # 4. 计算累积距离（TODO：使用cumulative_trapezoid）
        distance = cumulative_trapezoid(v, t, initial=0)

        # 5. 绘制图表
        plt.figure(figsize=(10, 6))
        plt.plot(t, v, 'b-', label='Velocity (m/s)')
        plt.plot(t, distance, 'r--', label='Distance (m)')
        plt.title('Velocity and Distance vs Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Velocity (m/s) / Distance (m)')
        plt.legend()
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print("错误：找不到数据文件")
        print("请确保数据文件存在于正确路径")

if __name__ == '__main__':
    main()
