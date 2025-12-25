import json
import base64
import os
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="PratibodhAI (प्रतिबोधAI)",
    page_icon="🕉️",
    layout="wide"  # Changed to wide for a more cinematic feel
)

# --------------------------------------------------
# CUSTOM CSS (THE UI MAGIC)
# --------------------------------------------------
# This CSS sets a dark theme, custom fonts, and a mystical background.
st.markdown("""
<style>
    /* 1. MAIN BACKGROUND */
    .stApp {
        background: radial-gradient(circle at 50% 10%, #2b1005, #000000);
        color: #e0e0e0;
    }
    
    /* 2. TEXT ELEMENTS */
    h1, h2, h3 {
        font-family: 'Cinzel', serif; /* Majestic font */
        color: #ffcc80 !important;
        text-align: center;
        text-shadow: 0px 0px 10px rgba(255, 204, 128, 0.5);
    }
    p {
        font-family: 'Lato', sans-serif;
        color: #b0bec5;
    }

    /* 3. INPUT AREA STYLING */
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.05);
        color: #fff;
        border: 1px solid #d35400;
        border-radius: 10px;
        font-size: 16px;
    }
    .stTextArea textarea:focus {
        border-color: #ff9800;
        box-shadow: 0 0 10px rgba(211, 84, 0, 0.5);
    }

    /* 4. BUTTON STYLING */
    .stButton button {
        background: linear-gradient(45deg, #d35400, #e67e22);
        color: white;
        border: none;
        padding: 12px 30px;
        font-size: 18px;
        border-radius: 25px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(211, 84, 0, 0.4);
        display: block;
        margin: 0 auto; /* Center button */
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(211, 84, 0, 0.6);
        background: linear-gradient(45deg, #e67e22, #d35400);
    }

    /* 5. CENTER THE LOGO */
    div[data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }
    
    /* 6. HIDE STREAMLIT FOOTER */
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HELPER: LOAD LOGO
# --------------------------------------------------
LOGO_PATH = "assets/logo.jpeg"

def load_logo(path):
    if not os.path.exists(path): return ""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

LOGO_B64 = load_logo(LOGO_PATH)

# --------------------------------------------------
# HEADER SECTION
# --------------------------------------------------
col1, col2, col3 = st.columns([1,2,1])

with col2:
    if LOGO_B64:
        st.markdown(
            f'<div style="display:flex; justify-content:center; margin-bottom:20px;">'
            f'<img src="data:image/jpeg;base64,{LOGO_B64}" style="width:120px; border-radius:50%; box-shadow: 0 0 20px rgba(255, 152, 0, 0.3);">'
            f'</div>',
            unsafe_allow_html=True
        )
    st.markdown("<h2>PratibodhAI (प्रतिबोधAI)</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center; font-size:1.1em; opacity:0.8;'>Reflect. Understand. Transcend.</p>", 
        unsafe_allow_html=True
    )

st.divider()

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
@st.cache_data
def load_verses():
    path = "data/Geeta.json"
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)["verses"]
    else:
        return [{
            "chapter": 2, "verse": 47, "reference": "BG 2.47",
            "sanskrit": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन...",
            "transliteration": "Karmanye vadhikaraste ma phaleshu kadachana...",
            "word_meanings": "Karma: Action... Phaleshu: In results...",
            "meaning_en": "You have a right to perform your prescribed duty, but you are not entitled to the fruits of action."
        }]

verses = load_verses()

# --------------------------------------------------
# AI MODEL
# --------------------------------------------------
contexts = [f"{v.get('meaning_en', '')} {v.get('sanskrit', '')}" for v in verses]

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

with st.spinner("Summoning wisdom..."):
    model = load_model()
    embeddings = model.encode(contexts, show_progress_bar=False)

# --------------------------------------------------
# LOGIC
# --------------------------------------------------
def explain_like_a_friend(user_input, verse_data):
    return (
        f"The ancient wisdom of <b>{verse_data.get('reference')}</b> resonates with your thoughts. "
        "It suggests that clarity is found not in fighting the current, but in understanding the flow. "
        "Observe the translation below."
    )

# --------------------------------------------------
# UI INTERACTION
# --------------------------------------------------
c1, c2, c3 = st.columns([1, 6, 1])
with c2:
    user_input = st.text_area(
        "Your Query",
        placeholder="What is weighing on your soul today?",
        height=100,
        label_visibility="collapsed"
    )
    
    # Center button hack
    st.write("")
    if st.button("Seek Reflection"):
        if not user_input.strip():
            st.warning("Please enter your thoughts first.")
        else:
            with st.spinner("Consulting the Gita..."):
                q_emb = model.encode([user_input])
                sims = cosine_similarity(q_emb, embeddings)[0]
                best_idx = int(np.argmax(sims))
                verse = verses[best_idx]

            # --------------------------------------------------
            # MODERN CARD UI (HTML/CSS)
            # --------------------------------------------------
            logo_bg = ""
            if LOGO_B64:
                logo_bg = f"url('data:image/jpeg;base64,{LOGO_B64}')"

            html_content = f"""
            <html>
            <head>
            <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Lato:ital,wght@0,300;0,400;1,400&display=swap" rel="stylesheet">
            <style>
                body {{
                    font-family: 'Lato', sans-serif;
                    background: transparent;
                    display: flex;
                    justify-content: center;
                    padding: 20px;
                }}
                /* GLASSMORPHISM CARD */
                .card {{
                    background: rgba(30, 30, 30, 0.6);
                    backdrop-filter: blur(12px);
                    -webkit-backdrop-filter: blur(12px);
                    border: 1px solid rgba(255, 255, 255, 0.1);
                    border-radius: 20px;
                    padding: 40px;
                    max-width: 750px;
                    width: 100%;
                    color: #fff;
                    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
                    position: relative;
                    overflow: hidden;
                    animation: fadeIn 1s ease-in-out;
                }}
                @keyframes fadeIn {{
                    from {{ opacity: 0; transform: translateY(20px); }}
                    to {{ opacity: 1; transform: translateY(0); }}
                }}
                
                /* DECORATIVE WATERMARK */
                .watermark {{
                    position: absolute;
                    top: -50px;
                    right: -50px;
                    width: 300px;
                    height: 300px;
                    background-image: {logo_bg};
                    background-size: contain;
                    background-repeat: no-repeat;
                    opacity: 0.05;
                    transform: rotate(20deg);
                    pointer-events: none;
                }}

                .header {{
                    text-align: center;
                    font-family: 'Cinzel', serif;
                    color: #ffb74d;
                    font-size: 28px;
                    margin-bottom: 20px;
                    letter-spacing: 2px;
                    text-transform: uppercase;
                    border-bottom: 1px solid rgba(255,183,77,0.3);
                    padding-bottom: 10px;
                }}

                .sanskrit {{
                    font-size: 24px;
                    text-align: center;
                    color: #fff;
                    font-weight: 500;
                    margin: 20px 0;
                    line-height: 1.6;
                }}

                .translit {{
                    text-align: center;
                    color: #b0bec5;
                    font-style: italic;
                    margin-bottom: 30px;
                    font-size: 16px;
                }}

                /* HIGHLIGHTED TRANSLATION BOX */
                .translation-box {{
                    background: rgba(211, 84, 0, 0.15); /* Orange Tint */
                    border-left: 4px solid #d35400;
                    padding: 20px;
                    border-radius: 8px;
                    margin: 20px 0;
                }}
                .translation-text {{
                    font-size: 18px;
                    line-height: 1.6;
                    color: #ffe0b2;
                }}

                .reflection {{
                    margin-top: 25px;
                    font-size: 16px;
                    color: #eceff1;
                    line-height: 1.6;
                    text-align: justify;
                }}

                .word-meanings {{
                    margin-top: 30px;
                    font-size: 14px;
                    color: #78909c;
                    border-top: 1px solid rgba(255,255,255,0.1);
                    padding-top: 15px;
                }}
            </style>
            </head>
            <body>
                <div class="card">
                    <div class="watermark"></div>
                    
                    <div class="header">Bhagavad Gita {verse.get('reference', '')}</div>
                    
                    <div class="sanskrit">{verse.get('sanskrit', '')}</div>
                    <div class="translit">{verse.get('transliteration', '')}</div>

                    <div class="translation-box">
                        <div class="translation-text">
                            "{verse.get('meaning_en', '')}"
                        </div>
                    </div>

                    <div class="reflection">
                        {explain_like_a_friend(user_input, verse)}
                    </div>

                    <div class="word-meanings">
                        <b>Word Breakdown:</b> {verse.get('word_meanings', '')}
                    </div>
                </div>
            </body>
            </html>
            """
            
            # Increased height for better view
            components.html(html_content, height=800, scrolling=False)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown(
    """
    <div style='text-align:center; color:#666; margin-top:50px; font-family: "Lato", sans-serif; font-size:12px;'>
        <p>PratibodhAI is an academic reflective system.<br>It does not provide moral, religious, or psychological advice.</p>
        <p style='color: #888; margin-top: 15px;'>Developed by <b>Sarthak Jain</b></p>
    </div>
    """,
    unsafe_allow_html=True
)