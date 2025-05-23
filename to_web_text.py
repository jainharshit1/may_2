# import streamlit as st
# import base64
# from pathlib import Path
# import streamlit.components.v1 as components

# # Streamlit page config
# st.set_page_config(page_title="🎁 Surprise Player", layout="centered")

# # ——— 1) Load & encode video ———
# video_path = Path("PortraitThenBow.mp4")
# if not video_path.exists():
#     st.error("❌ PortraitThenBow.mp4 not found.")
#     st.stop()
# video_b64 = base64.b64encode(video_path.read_bytes()).decode()

# # ——— 2) Load & “class up” your SVGs ———
# def inject_attrs(svg_text, attrs):
#     # inject attrs into the first <svg ...> tag
#     return svg_text.replace(
#         "<svg",
#         "<svg " + " ".join(f'{k}="{v}"' for k,v in attrs.items()),
#         1
#     )

# # main “happy birthday” text
# svg_path = Path("hbday_text.svg")
# if not svg_path.exists():
#     st.error("❌ hbday_text.svg not found.")
#     st.stop()
# svg_text = svg_path.read_text()
# svg_main = inject_attrs(svg_text, {"class":"mainText"})

# # chotu text (hidden until last 5s)
# chotu_path = Path("ch.svg")
# if not chotu_path.exists():
#     st.error("❌ ch.svg not found.")
#     st.stop()
# chotu_text = chotu_path.read_text()
# svg_chotu = inject_attrs(chotu_text, {"class":"chotuText", "id":"chotuText"})

# # ——— 3) Build HTML/CSS/JS ———
# html = f"""
# <style>
#   .player-container {{
#     position: relative; width: 100%; max-width: 800px;
#     aspect-ratio: 16/9; margin: auto; overflow: hidden;
#     background: #000;
#   }}
#   .player-container video {{
#     width: 100%; height: 100%; display: block;
#   }}
#   #playBtn {{
#     position: absolute; top: 50%; left: 50%;
#     transform: translate(-50%,-50%);
#     z-index: 3;
#     background: rgba(0,0,0,0.6); border: none;
#     color: white; font-size: 2rem;
#     padding: 0.5em 1.2em; border-radius: 8px;
#     cursor: pointer; display: flex;
#     align-items: center;
#   }}
#   #controlsOverlay {{
#     position: absolute; top: 0; left: 0;
#     width: 100%; height: 100%; z-index: 3;
#     background: rgba(0,0,0,0.5);
#     display: flex; justify-content: center;
#     align-items: center;
#   }}
#   .textOverlay {{
#     position: absolute; top: 0; left: 0;
#     width: 100%; height: 100%;
#     stroke: black;
#     fill: black !important;
#     pointer-events: none; z-index: 2;
#   }}
#   /* main stroke-draw text */
#   .textOverlay svg.mainText {{
#     position: absolute; top: 0; left: 0;
#     width: 45%; height: 70%; margin: 9px;
#   }}
#   /* chotu text—hidden then fade in */
#   .textOverlay svg.chotuText {{
#     position: absolute; bottom: 10%; right: 5%;
#     width: 30%; height: auto;
#     stroke: black; stroke-width: 4;
#     opacity: 0; transition: opacity 1s ease-in-out;
#   }}
#   /* left “happy birthday”: outline only */
#   .textOverlay svg.mainText path {{
#     stroke: black;
#     stroke-width: 4;
#     fill: none;
#   }}

#   /* right “chotu”: bold solid black */
#   .textOverlay svg.chotuText path {{
#     stroke: black;
#     stroke-width: 4;
#     fill: black;
#   }}
# </style>

# <div class="player-container">
#   <video id="bgvid" controls muted playsinline>
#     <source src="data:video/mp4;base64,{video_b64}" type="video/mp4">
#   </video>
#   <div id="controlsOverlay">
#     <button id="playBtn">
#       <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor">
#         <polygon points="8,5 19,12 8,19"/>
#       </svg>
#       🎁 Surprise
#     </button>
#   </div>
#   <div class="textOverlay">
#     {svg_main}
#     {svg_chotu}
#   </div>
# </div>

# <script>
#   document.addEventListener("DOMContentLoaded", () => {{
#     const video = document.getElementById("bgvid"),
#           overlay = document.getElementById("controlsOverlay"),
#           btn = document.getElementById("playBtn"),
#           mainSvg = document.querySelector("svg.mainText"),
#           paths = mainSvg.querySelectorAll("path"),
#           chotu = document.getElementById("chotuText");

#     // prepare stroke-dash
#     paths.forEach(p => {{
#       const L = p.getTotalLength();
#       p.style.strokeDasharray = L;
#       p.style.strokeDashoffset = L;
#     }});

#     btn.addEventListener("click", () => {{
#       overlay.style.display = "none";
#       video.play();

#       // animate drawing over the actual video duration
#       const drawDuration = (video.duration || 10) * 5000; 
#       paths.forEach(p => {{
#         const L = p.getTotalLength();
#         p.animate(
#           [ {{ strokeDashoffset: L }}, {{ strokeDashoffset: 0 }} ],
#           {{ duration: drawDuration, fill: "forwards", easing: "linear" }}
#         );
#       }});
#     }});

#     // fade in chotu in last 5s
#     video.addEventListener("timeupdate", () => {{
#       if (video.duration - video.currentTime <= 5) {{
#         chotu.style.opacity = 1;
#       }} else {{
#         chotu.style.opacity = 0;
#       }}
#     }});
#   }});
# </script>
# """

# components.html(html, height=500, scrolling=False)

import streamlit as st
import base64
from pathlib import Path
import streamlit.components.v1 as components

# Streamlit page config
st.set_page_config(page_title="🎁 Surprise Player", layout="centered")

# ——— 1) Load & encode video ———
video_path = Path("PortraitThenBow.mp4")
if not video_path.exists():
    st.error("❌ PortraitThenBow.mp4 not found.")
    st.stop()
video_b64 = base64.b64encode(video_path.read_bytes()).decode()

# ——— 2) Load & “class up” your SVGs ———
def inject_attrs(svg_text, attrs):
    return svg_text.replace(
        "<svg",
        "<svg " + " ".join(f'{k}="{v}"' for k, v in attrs.items()),
        1
    )

svg_main = inject_attrs(Path("hbday_text.svg").read_text(), {"class": "mainText"})
svg_chotu = inject_attrs(Path("ch.svg").read_text(), {"class": "chotuText", "id": "chotuText"})

# ——— 3) Build HTML/CSS/JS ———
html = f"""
<style>
  .player-container {{ position: relative; width: 100%; max-width: 800px;
                       aspect-ratio: 16/9; margin: auto; overflow: hidden; background: #000; }}
  .player-container video {{ width: 100%; height: 100%; display: block; }}
  #playBtn {{ position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%);
              z-index: 3; background: rgba(0,0,0,0.6); border: none; color: white;
              font-size: 2rem; padding: 0.5em 1.2em; border-radius: 8px;
              cursor: pointer; display: flex; align-items: center; }}
  #controlsOverlay {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%;
                     z-index: 3; background: rgba(0,0,0,0.5);
                     display: flex; justify-content: center; align-items: center; }}
  .textOverlay {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%;
                  pointer-events: none; z-index: 2; }}
  .textOverlay svg.mainText path {{ stroke: black; stroke-width: 4; fill: none; }}
  .textOverlay svg.chotuText path {{ stroke: black; stroke-width: 4; fill: black; }}
  .textOverlay svg.mainText {{ position: absolute; top: 0; left: 0;
                               width: 45%; height: 70%; margin: 9px; }}
  .textOverlay svg.chotuText {{ position: absolute; bottom: 10%; right: 5%;
                                width: 30%; height: auto;
                                opacity: 0; transition: opacity 1s ease-in-out; }}

  /* Notes wrapper (outside player) */
  .notes-wrapper {{ margin: 1.5em auto; max-width: 800px;
                   display: flex; flex-direction: column; align-items: flex-start; gap: 0.5em; }}
  .note-btn {{ padding: 0.5em 1em; font-size: 1rem; border: none;
               border-radius: 1em; background: linear-gradient(135deg, #4A90E2, #357ABD);
               color: white; cursor: pointer; }}
  .note-overlay {{ background: rgba(0,0,0,0.9); color: white; padding: 1em;
                   border-radius: 0.5em; font-size: 1.1rem; display: none;
                   white-space: pre-wrap; /* wrap long text */ 
                   font-family: 'Brittany', cursive;}}
  .note-overlay button {{ margin-left: 1em; padding: 0.3em 0.8em; font-size: 0.9rem;
                          border: none; border-radius: 0.5em; background: #357ABD;
                          color: white; cursor: pointer; }}
</style>

<div class="player-container">
  <video id="bgvid" controls muted playsinline>
    <source src="data:video/mp4;base64,{video_b64}" type="video/mp4">
  </video>
  <div id="controlsOverlay">
    <button id="playBtn">🎁 Surprise</button>
  </div>
  <div class="textOverlay">
    {svg_main}
    {svg_chotu}
  </div>
</div>

<div class="notes-wrapper">
  <button id="noteBtn1" class="note-btn">Show Note</button>
  <div id="note1" class="note-overlay">
    To the strongest and smartest girl:
       A very Happy Birthday Doxaab! 🎉
       May this year fill beautful colours in your life.
    Pehle to  sorry doxaab bina puche aapki profile photo use karli thi is 
    animation ke liye but I hope you like it and just wanted you to know that,
        I am waiting for you and for "I think the time is not right" se
        "Now I think the time is right" ho jane ka.
    <button id="noteBtn2">Show Next Note</button>
  </div>
  <div id="note2" class="note-overlay">
    Bas abhi itna hi. baki baatein aapse milke hi karenge, jyda time nhi lunga aapka
    pata lage aaj bhi koi paper ho 🤦
    hope to see you soon.
  </div>
</div>

<script>
  document.addEventListener("DOMContentLoaded", () => {{
    const video    = document.getElementById("bgvid"),
          overlay  = document.getElementById("controlsOverlay"),
          btn      = document.getElementById("playBtn"),
          paths    = document.querySelectorAll("svg.mainText path"),
          chotu    = document.getElementById("chotuText"),
          noteBtn1 = document.getElementById("noteBtn1"),
          noteBtn2 = document.getElementById("noteBtn2"),
          note1    = document.getElementById("note1"),
          note2    = document.getElementById("note2");

    // prepare stroke-dash
    paths.forEach(p => {{
      const L = p.getTotalLength();
      p.style.strokeDasharray  = L;
      p.style.strokeDashoffset = L;
    }});

    btn.addEventListener("click", () => {{
      overlay.style.display = "none";
      video.play();
      const drawDuration = (video.duration || 10) * 5000;
      paths.forEach(p => {{
        const L = p.getTotalLength();
        p.animate(
          [{{ strokeDashoffset: L }}, {{ strokeDashoffset: 0 }}],
          {{ duration: drawDuration, fill: "forwards", easing: "linear" }}
        );
      }});
    }});

    // fade in chotu in last 5s
    video.addEventListener("timeupdate", () => {{
      chotu.style.opacity = (video.duration - video.currentTime <= 5) ? 1 : 0;
    }});

    // Note 1
    noteBtn1.addEventListener("click", () => {{
      note1.style.display    = "block";
      noteBtn1.disabled      = true;
    }});

    // Note 2
    noteBtn2.addEventListener("click", () => {{
      note2.style.display   = "block";
      noteBtn2.disabled     = true;
    }});
  }});
</script>
"""

components.html(html, height=900, scrolling=False)
