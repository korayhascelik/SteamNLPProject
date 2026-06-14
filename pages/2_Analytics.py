import streamlit as st
import plotly.express as px

from utils.loader import load_data
from utils.theme import apply_theme

apply_theme()

df = load_data()

st.markdown(
    """
    <div class="hero-card">
        <h1>📈 Analytics</h1>
        <p class="hero-description">
            Sentiment, oynama süresi ve kelime sayısı dağılımlarını etkileşimli grafiklerle keşfedin.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

tab1, tab2, tab3 = st.tabs([
    "Sentiment",
    "Playtime",
    "Word Count"
])

with tab1:
    fig = px.histogram(df, x="sentiment_polarity", nbins=40, title="Sentiment Dağılımı")
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    fig = px.histogram(df, x="playtime_forever", nbins=40, title="Playtime Dağılımı")
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    fig = px.histogram(df, x="word_count", nbins=40, title="Word Count Dağılımı")
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)
