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

st.set_page_config(page_title="📚 Artikel Suggestie", layout="centered")

st.title("📖 Willekeurige Artikel Suggestie")

articles = load_articles()

if not articles:
    st.warning("Geen artikels gevonden. Voeg eerst artikels toe aan de JSON.")
else:
    if st.button("🎲 Toon een willekeurig artikel"):
        article = random.choice(articles)
        st.subheader(article['title'])
        st.markdown(f"[🌐 Lees artikel]({article['url']})")

    st.markdown(f"📄 Totaal artikels: **{len(articles)}**")