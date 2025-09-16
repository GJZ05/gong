import streamlit as st

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
    else:
        st.error("生日不对哦~")
        st.stop()  # 停止程序



from turtle import *
import time

speed(0)
color('red', 'pink')

begin_fill()
left(140)
forward(111.65)

def curvemove():
    for i in range(100):
        right(2)
        forward(2)

curvemove()
left(120)
curvemove()
forward(111.65)
end_fill()

hideturtle()

penup()
goto(0, -50)
pendown()

color('black')
# 使用中文字体确保正确显示
write('尊敬的VIP,小的为您服务！', align="center", font=("SimHei", 16, "normal"))

time.sleep(3)

