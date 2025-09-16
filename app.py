import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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
        
        # 使用matplotlib绘制心形图案
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # 生成心形曲线数据
        t = np.linspace(0, 2 * np.pi, 1000)
        x = 16 * np.sin(t)**3
        y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
        
        # 绘制心形并填充
        ax.fill(x, y, color='pink', edgecolor='red', linewidth=2)
        
        # 添加文本（调整y值将文本放在爱心底部）
        ax.text(0, -20, f'尊敬的VIP,小的为您服务！', 
                ha='center', va='center', fontsize=16, color='black')
        
        # 设置坐标轴范围和隐藏坐标轴
        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 15)  # 调整y轴范围使爱心显示更完整
        ax.axis('off')
        
        # 在Streamlit中显示图形
        st.pyplot(fig)
        
    else:
        st.error("生日不对哦~")
        st.stop()  # 停止程序
    

