import streamlit as st
import plotly.graph_objects as go

from utils.feature_engineering import create_features
from utils.loader import load_model, load_scaler
from utils.theme import apply_theme

apply_theme()

model = load_model()
scaler = load_scaler()

# 9 feature'ın sırası (create_features'daki sıra)
ALL_FEATURES_ORDER = [
    'playtime_x_word_count',
    'playtime_x_sentiment_polarity',
    'word_count_x_sentiment_polarity',
    'sentiment_ratio',
    'engagement_score',
    'polarity_intensity',
    'has_positive_sentiment',
    'has_negative_sentiment',
    'is_very_subjective'
]

# Model'in kullandığı 7 feature (unscaled adları)
SELECTED_FEATURES_UNSCALED = [
    'playtime_x_sentiment_polarity',
    'word_count_x_sentiment_polarity',
    'sentiment_ratio',
    'polarity_intensity',
    'has_positive_sentiment',
    'has_negative_sentiment',
    'engagement_score'
]

SELECTED_INDICES = [ALL_FEATURES_ORDER.index(feat) for feat in SELECTED_FEATURES_UNSCALED]

st.markdown(
    """
    <div class="hero-card">
        <h1>🤖 Prediction Center</h1>
        <p class="hero-description">
            İnceleme metni ve oynama süresi verilerini kullanarak oyunun önerilip önerilmeyeceğini tahmin edin.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([2, 1], gap="large")

with left:
    with st.form(key="prediction_form"):
        review = st.text_area(
            "Review",
            height=220,
            placeholder="Örnek: Bu oyun son derece eğlenceliydi, kesinlikle tavsiye ederim...",
        )
        playtime = st.number_input("Playtime (saat)", min_value=0, value=120, step=10)
        predict_button = st.form_submit_button("Tahmin Et")

    if predict_button:
        features = create_features(review, playtime)
        scaled_array = scaler.transform(features)
        scaled_selected = scaled_array[:, SELECTED_INDICES]

        pred = model.predict(scaled_selected)[0]
        prob = model.predict_proba(scaled_selected)[0].max()

        card_title = "Tahmin Sonucu"
        if pred == 1:
            st.success(f"Öneriliyor ({prob:.2%})")
        else:
            st.error(f"Önerilmiyor ({prob:.2%})")

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=prob * 100,
                title={"text": "Confidence"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "#2563eb"},
                    "bgcolor": "rgba(255,255,255,0.04)",
                },
            )
        )
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#e2e8f0"))

        st.plotly_chart(fig, use_container_width=True)

with right:
    st.markdown(
        """
        <div class="panel-card">
            <h2>Nasıl çalışır?</h2>
            <ul>
                <li>Metin duygu analizi ve kelime sayısı değerlerini hesaplar.</li>
                <li>Oynama süresi ile sentiment kombinasyonları değerlendirir.</li>
                <li>Model, oyun önerisini yüzde olarak güvenirlik skoruyla sunar.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.info(
        "Model, ifadelerdeki duyguyu ve oynama süresi verisini kullanarak tavsiye kararını tahmin eder."
    )
