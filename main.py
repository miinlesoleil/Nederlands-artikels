import streamlit as st
import json
import random
import os

FILE_PATH = "manual_articles.json"

# Load articles
def load_articles():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Page config
st.set_page_config(
    page_title="📚 Artikel Suggestie",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom style
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Times New Roman', Times, serif !important;
    }

    .stApp {
        background-color: #f8f1e4;
    }

    h1, h2, h3 {
        color: #2b2b2b;
    }

    .stButton>button {
        color: #f8f1e4;
        background-color: #5a4d41;
        border: none;
        padding: 0.6em 1.2em;
        font-size: 1em;
        border-radius: 8px;
    }

    .stButton>button:hover {
        background-color: #776556;
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("# ✨ *Willekeurige Artikel Suggestie*")
st.markdown("### _Hier zijn wij fan van EOS Wetenschap Artikels!_")
st.markdown("🕯️ *Veel succes met je ITNA examen*💘")
articles = load_articles()

if not articles:
    st.warning("Geen artikels gevonden. Voeg eerst artikels toe aan de JSON.")
else:
    if st.button("📜 Toon een artikel"):
        article = random.choice(articles)
        st.markdown("### 📖 " + article['title'])
        st.markdown(f"🔗 [Lees dit artikel]({article['url']})")

    st.markdown(f"🗂️ In totaal zijn er **{len(articles)}** artikels.")
