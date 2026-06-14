import streamlit as st

from utils.loader import load_data
from utils.theme import apply_theme

st.set_page_config(
    page_title="Steam Review Intelligence",
    page_icon="🎮",
    layout="wide"
)

apply_theme()

df = load_data()
total = len(df)
positive = (df["voted_up"] == True).sum()
negative = (df["voted_up"] == False).sum()
ratio = positive / total * 100

st.markdown(
    """
    <div class="hero-card">
        <h1>Steam Review Intelligence</h1>
        <p class="hero-description">
            Oyun incelemelerini analiz eden, model performansı ve açıklanabilirlik sunan modern bir Streamlit uygulaması.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([3, 1], gap="large")

with col1:
    st.subheader("Hızlı Bakış")
    st.markdown(
        """
        - İnceleme metinleri üzerinden kullanıcı öneri tahmini.
        - Görselleştirilmiş performans ve analiz sayfaları.
        - Model açıklamaları ile güvenilir içgörüler.
        """
    )

with col2:
    st.metric("Toplam İnceleme", f"{total:,}")
    st.metric("Olumlu İnceleme", f"{positive:,}")
    st.metric("Olumsuz İnceleme", f"{negative:,}")
    st.metric("Olumlu Oran", f"{ratio:.2f}%")

st.markdown("---")

st.subheader("Kısa Yol")
st.write(
    "Sol taraftaki sayfa menüsünden istediğiniz bölüme geçerek tahmin, analiz ve performans raporlarına ulaşabilirsiniz."
)