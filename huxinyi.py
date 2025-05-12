import streamlit as st
import random

# 页面设置
st.set_page_config(page_title="胡欣怡专属调侃生成器", page_icon="🎉", layout="centered")

# CSS样式（渐变背景和按钮样式）
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #ff66b2, #f5e6ff);  /* 渐变背景：从粉色到浅紫色 */
            background-size: cover;
        }
        .big-button {
            background-color: #ff66b2;
            color: white;
            font-size: 18px;
            padding: 15px 30px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .big-button:hover {
            background-color: #ff3399;
            transform: scale(1.1);
        }
        .stars {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
        }
        .star {
            position: absolute;
            width: 5px;
            height: 5px;
            background-color: white;
            border-radius: 50%;
            animation: star-flicker 1.5s infinite;
        }
        @keyframes star-flicker {
            0% { opacity: 0; }
            50% { opacity: 1; }
            100% { opacity: 0; }
        }
    </style>
""", unsafe_allow_html=True)

# 创建动态星星
st.markdown("""
    <div class="stars">
        <div class="star" style="top: 20%; left: 30%; animation-delay: 0s;"></div>
        <div class="star" style="top: 40%; left: 70%; animation-delay: 0.5s;"></div>
        <div class="star" style="top: 60%; left: 20%; animation-delay: 1s;"></div>
        <div class="star" style="top: 80%; left: 50%; animation-delay: 1.5s;"></div>
        <div class="star" style="top: 10%; left: 90%; animation-delay: 2s;"></div>
    </div>
""", unsafe_allow_html=True)

# 页面标题
st.title("🎉 胡欣怡今日智能点评 ✨")

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

# 点击按钮生成调侃（更新按钮样式和调侃文本）
if st.button("来一段今天的胡式调侃吧 😏", key="generate_joke", help="点击我！你会笑出声！", use_container_width=True):
    st.success(random.choice(jokes))

# 自动播放背景音乐
audio_html = """
<audio autoplay loop>
  <source src="https://m8.music.126.net/20250512235521/280333bb1c287a8ee86da14886b3ef58/ymusic/9a8f/c475/4fb1/de0bb6a857c5b3647c17259416f16572.mp3">
  Your browser does not support the audio element.
</audio>
"""
st.markdown(audio_html, unsafe_allow_html=True)
