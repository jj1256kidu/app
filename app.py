import streamlit as st

# Set page config
st.set_page_config(page_title="Neon Login", layout="centered", page_icon="🔐")

# Custom CSS for neon look
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap');

    body {
        background: radial-gradient(circle at center, #0d0d1a, #05010a);
    }

    .stApp {
        background: radial-gradient(circle at center, #0d0d1a, #05010a);
        font-family: 'Orbitron', sans-serif;
        color: #00f7ff;
    }

    .login-box {
        background-color: rgba(0, 0, 0, 0.85);
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 0 20px #00e6ff;
        text-align: center;
        width: 400px;
        margin: 100px auto;
    }

    input, .stTextInput > div > div > input {
        background-color: #111 !important;
        color: white !important;
        border-radius: 30px !important;
        padding: 10px 20px !important;
        border: none !important;
        box-shadow: 0 0 10px #00ffff !important;
    }

    .login-button > button {
        width: 100%;
        padding: 12px;
        border: none;
        border-radius: 30px;
        background: linear-gradient(to right, #00f0ff, #d946ef);
        color: white;
        font-size: 16px;
        cursor: pointer;
        transition: 0.3s;
        font-family: 'Orbitron', sans-serif;
    }

    .login-button > button:hover {
        background: linear-gradient(to right, #d946ef, #00f0ff);
    }

    .remember {
        color: #ccc;
        font-size: 13px;
        margin-top: 10px;
    }

    .forgot {
        text-align: right;
        margin-top: 10px;
        font-size: 13px;
    }

    .forgot a {
        color: #77dfff;
        text-decoration: none;
    }

    h2 {
        color: #00f7ff;
        font-size: 28px;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Login layout
st.markdown('<div class="login-box">', unsafe_allow_html=True)
st.markdown('<h2>Welcome Back</h2>', unsafe_allow_html=True)

username = st.text_input("Username", placeholder="Enter your username")
password = st.text_input("Password", type="password", placeholder="Enter your password")

remember = st.checkbox("Remember me")

login_clicked = st.button("Login", type="primary")

if login_clicked:
    if username and password:
        st.success(f"Welcome, {username}!")
    else:
        st.error("Please enter both username and password.")

st.markdown('<div class="forgot"><a href="#">Forgot password?</a></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
