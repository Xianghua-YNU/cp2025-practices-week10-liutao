import numpy as np
from scipy.integrate import cumulative_trapezoid
import matplotlib.pyplot as plt
import os

def main():
    try:
        # 1. 获取数据文件路径（TODO：使用绝对路径）
        data_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        data_file = os.path.join(data_dir, 'Velocities.txt')
        
        # 调试信息
        print(f"[DEBUG] 当前工作目录: {os.getcwd()}")
        print(f"[DEBUG] 脚本所在目录: {data_dir}")
        print(f"[DEBUG] 文件完整路径: {data_file}")

        # 检查文件是否存在
        if not os.path.exists(data_file):
            raise FileNotFoundError(f"错误：文件 {os.path.abspath(data_file)} 不存在！")
        # 2. 读取数据（TODO：使用numpy.loadtxt）
        try:
            data = np.loadtxt(data_file)
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
