# hu_xinyi_app.py
import streamlit as st
import random

# 页面设置
st.set_page_config(page_title="胡欣怡专属调侃生成器", page_icon="🎉", layout="centered")

st.title("🎉 胡欣怡今日智能点评")

# 调侃语句列表
jokes = [
    "胡欣怡今天太聪明了，以至于连老师都不敢提问。",
    "胡欣怡的可爱程度，足以击败全国99%的猫。",
    "她一出场，Wi-Fi 信号都强了三格。",
    "据说，拖延症是遇到她后才觉得自己效率太高。",
    "如果胡欣怡考试前临时抱佛脚，佛都会给她让座。",
    "她说不想学习的时候，连书本都开始颤抖。",
    "天塌下来有高个子顶着，但她选择穿高跟鞋硬刚。",
    "胡欣怡的生活原则：既美丽又懒惰，是一种信仰。",
]

# 点击按钮生成调侃
if st.button("生成今日调侃"):
    st.success(random.choice(jokes))

# 自动播放背景音乐
audio_html = """
<audio autoplay loop>
  <source src="https://m8.music.126.net/20250512235521/280333bb1c287a8ee86da14886b3ef58/ymusic/9a8f/c475/4fb1/de0bb6a857c5b3647c17259416f16572.mp3">
  Your browser does not support the audio element.
</audio>
"""
st.markdown(audio_html, unsafe_allow_html=True)