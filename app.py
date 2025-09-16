import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter  # 导入PillowWriter
import io
from PIL import Image

# 设置中文字体
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]

st.title("某人的专属小程序")

# 名字输入
name = st.text_input("请输入宝宝的名字")

# 生日输入
birthday = st.text_input("请输入宝宝的生日")

# 验证输入
if name and birthday:
    # 校验名字：只允许 "叶少芸"
    if name != "叶少芸":
        st.error("名字不对哦~")
        st.stop()  # 停止程序
    
    # 校验生日：只允许 6月23日 或 6.23
    formatted_birthday = birthday.replace("月", ".").replace("日", "")
    if formatted_birthday == "6.23":
        st.success(f"你来啦，{name}VIP！")
        st.balloons()  # 添加庆祝动画
        
        # 创建图形和轴
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # 生成心形曲线完整数据
        t = np.linspace(0, 2 * np.pi, 1000)
        x = 16 * np.sin(t)**3
        y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
        
        # 设置坐标轴范围和隐藏坐标轴
        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 15)
        ax.axis('off')
        
        # 初始化线条和填充对象
        line, = ax.plot([], [], color='red', linewidth=2)
        fill = ax.fill([], [], color='pink', alpha=0.7)
        
        # 添加文本（先隐藏，绘制完成后显示）
        text = ax.text(0, -20, f'尊敬的VIP,小的为您服务！', 
                ha='center', va='center', fontsize=16, color='black', alpha=0)
        
        # 动画更新函数
        def update(frame):
            # 确定当前帧要显示的数据量（总帧数的百分比）
            percent = frame / 100.0
            end_idx = int(len(t) * percent)
            
            # 更新线条数据
            line.set_data(x[:end_idx], y[:end_idx])
            
            # 更新填充区域
            if end_idx > 0:
                # 清除之前的填充
                for f in fill:
                    f.remove()
                # 创建新的填充
                fill[0] = ax.fill(x[:end_idx], y[:end_idx], color='pink', alpha=0.7)[0]
            
            # 当绘制完成时显示文本
            if percent >= 1.0:
                text.set_alpha(1.0)
                
            return line, fill[0], text
        
        # 创建动画（100帧，每帧50ms，总时长5秒）
        ani = FuncAnimation(fig, update, frames=101, interval=50, blit=True)
        
        # 创建PillowWriter并指定格式
        writer = PillowWriter(fps=20)  # 设置帧率
        
        # 将动画保存到缓冲区
        buf = io.BytesIO()
        ani.save(buf, writer=writer, savefig_kwargs={'bbox_inches': 'tight'})
        buf.seek(0)
        
        # 显示动画
        st.image(Image.open(buf))
        
    else:
        st.error("生日不对哦~")
        st.stop()  # 停止程序
