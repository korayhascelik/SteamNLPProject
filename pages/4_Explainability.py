import streamlit as st
from utils.theme import apply_theme

apply_theme()

st.markdown(
    """
    <div class="hero-card">
        <h1>🧠 Explainability</h1>
        <p class="hero-description">
            Model kararlarının hangi özelliklere dayandığını açık ve anlaşılır bir biçimde görün.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="panel-card">
        <h2>Model Kullanılan Özellikler</h2>
        <ul>
            <li>sentiment_polarity</li>
            <li>playtime_x_sentiment_polarity</li>
            <li>polarity_intensity</li>
            <li>sentiment_ratio</li>
            <li>has_positive_sentiment</li>
            <li>has_negative_sentiment</li>
            <li>word_count_x_sentiment_polarity</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)
