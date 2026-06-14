import streamlit as st
import pandas as pd
from utils.theme import apply_theme

apply_theme()

st.markdown(
    """
    <div class="hero-card">
        <h1>🏆 Model Performance</h1>
        <p class="hero-description">
            Modelinizin doğruluk ve dengeli performans metriklerini modern bir görselle keşfedin.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

metrics = pd.DataFrame({
    "Metric": ["Accuracy", "Precision", "Recall", "F1"],
    "Value": [0.91, 0.90, 0.91, 0.90],
})

st.markdown(
    """
    <div class="panel-card">
        <h2>Performans Özeti</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

st.dataframe(metrics, use_container_width=True)
performance_chart = metrics.set_index("Metric")
st.bar_chart(performance_chart)
