import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Neon Login", layout="centered", page_icon="✨")

# Inject particles.js animation
components.html("""
<!DOCTYPE html>
<html>
<head>
  <style>
    body, html {
      margin: 0;
      padding: 0;
      overflow: hidden;
    }
    #tsparticles {
      position: fixed;
      width: 100%;
      height: 100%;
      z-index: -1;
    }
  </style>
  <script src="https://cdn.jsdelivr.net/npm/tsparticles@3/tsparticles.bundle.min.js"></script>
</head>
<body>
  <div id="tsparticles"></div>
  <script>
    tsParticles.load("tsparticles", {
      background: { color: { value: "#05010a" } },
      fpsLimit: 60,
      interactivity: {
        events: { onHover: { enable: true, mode: "repulse" }, resize: true },
        modes: { repulse: { distance: 100, duration: 0.4 } }
      },
      particles: {
        color: { value: ["#00f0ff", "#d946ef", "#ffcc00", "#00ff99"] },
        links: { enable: true, color: "#ffffff", distance: 150, opacity: 0.2 },
        collisions: { enable: false },
        move: { enable: true, speed: 1, direction: "none", random: true, straight: false, bounce: false },
        number: { value: 60, density: { enable: true, area: 800 } },
        opacity: { value: 0.5 },
        shape: { type: "circle" },
        size: { value: { min: 2, max: 4 } }
      },
      detectRetina: true
    });
  </script>
</body>
</html>
""", height=0)

# Custom Neon CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap');

    .stApp {
        background-color: transparent;
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
        margin: 120px auto;
    }

    input, .stTextInput > div > div > input {
        background-color: #111 !important;
        color: white !important;
        border-radius: 30px !important;
        padding: 10px 20px !important;
        border: none !important;
        box-shadow: 0 0 10px #00ffff !important;
    }

    .stButton > button {
        width: 100%;
        padding: 12px;
        border: none;
        border-radius: 30px;
        background: linear-gradient(to right, #00f0ff, #d946ef);
        color: white;
        font-size: 16px;
        cursor: pointer;
        font-family: 'Orbitron', sans-serif;
        margin-top: 20px;
    }

    .stButton > button:hover {
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

# Login UI
st.markdown('<div class="login-box">', unsafe_allow_html=True)
st.markdown('<h2>Welcome Back</h2>', unsafe_allow_html=True)

username = st.text_input("Username", placeholder="Enter your username")
password = st.text_input("Password", type="password", placeholder="Enter your password")

remember = st.checkbox("Remember me")

login_clicked = st.button("Login")

if login_clicked:
    if username and password:
        st.success(f"Welcome, {username}!")
    else:
        st.error("Please enter both username and password.")

st.markdown('<div class="forgot"><a href="#">Forgot password?</a></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
