import streamlit as st
from utils.loader import load_data
from utils.theme import apply_theme

apply_theme()

df = load_data()

total = len(df)
positive = (df["voted_up"] == True).sum()
negative = (df["voted_up"] == False).sum()
ratio = positive / total * 100

st.markdown(
    """
    <div class="hero-card">
        <h1>📊 Dashboard</h1>
        <p class="hero-description">
            Veri setindeki ana eğilimleri hızlıca inceleyin. Olumlu/olumsuz dağılım ve genel performans metriklerine profesyonel bir bakış sağlayın.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

c1, c2, c3, c4 = st.columns(4, gap="large")

c1.metric("Toplam İnceleme", f"{total:,}")
c2.metric("Olumlu", f"{positive:,}")
c3.metric("Olumsuz", f"{negative:,}")
c4.metric("Olumlu %", f"{ratio:.2f}%")