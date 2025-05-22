import streamlit as st
import streamlit.components.v1 as components
import base64

# Page setup
st.set_page_config(page_title="🎁 Surprise Player", layout="centered")
st.markdown("", unsafe_allow_html=True)

# Load & encode video
video_path = "PortraitThenBow.mp4"
with open(video_path, "rb") as f:
    video_bytes = f.read()
    video_base64 = base64.b64encode(video_bytes).decode()

# Build responsive HTML/CSS/JS
html_code = f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
      .video-container {{
        position: relative;
        width: 100%;
        max-width: 700px;
        margin: 0 auto;
      }}
      #myVideo {{
        width: 100%;
        height: auto;
        border-radius: 12px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.6);
      }}
      .overlay {{
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: rgba(0,0,0,0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 2;
      }}
      .play-button {{
        background: #ff4b85;
        color: white;
        font-size: 5vw;        /* scales on mobile */
        min-font-size: 18px;   /* never too small */
        border: none;
        border-radius: 8px;
        padding: 1em 2em;
        cursor: pointer;
        display: flex;
        align-items: center;
      }}
      .play-button svg {{
        width: 1em;
        height: 1em;
        margin-right: 0.5em;
      }}
    </style>
  </head>
  <body>
    <div class="video-container">
      <video id="myVideo" controls>
        <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <div class="overlay" id="overlay">
        <button class="play-button" onclick="playVideo()">
          <!-- Inline SVG for a crisp ▶ icon -->
          <svg viewBox="0 0 24 24" fill="currentColor">
            <polygon points="8,5 19,12 8,19" />
          </svg>
          Surprise
        </button>
      </div>
    </div>

    <script>
      function playVideo() {{
        const vid = document.getElementById("myVideo");
        document.getElementById("overlay").style.display = "none";
        vid.play();
      }}
    </script>
  </body>
</html>
"""

# Render
components.html(html_code, height=600)

