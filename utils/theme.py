import streamlit as st

def apply_theme():
    st.markdown(
        """
        <style>
        :root {
          color-scheme: dark;
          font-family: Inter, ui-sans-serif, system-ui, sans-serif;
        }

        .stApp {
          background: radial-gradient(circle at top left, #111827 0%, #0f172a 40%, #030712 100%);
          color: #e2e8f0;
        }

        section[data-testid="stSidebar"] {
          background: #0f172a;
          border-right: 1px solid rgba(148, 163, 184, 0.12);
        }

        .st-bb, .st-ds {
          background: transparent;
        }

        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5 {
          color: #f8fafc;
        }

        .stMarkdown p, .stMarkdown li, .stText, .stText span {
          color: #cbd5e1;
        }

        .stButton > button {
          background-color: #2563eb;
          border: 1px solid rgba(37, 99, 235, 0.85);
          color: #ffffff;
          border-radius: 999px;
          padding: 0.75rem 1.25rem;
          font-weight: 600;
        }

        .stButton > button:hover {
          background-color: #1d4ed8;
        }

        .stTextInput>div>div>input,
        .stNumberInput>div>div>input,
        textarea {
          background: rgba(255, 255, 255, 0.05);
          border: 1px solid rgba(148, 163, 184, 0.22);
          border-radius: 12px;
          color: #e2e8f0;
        }

        .stTextInput>label, .stNumberInput>label, .stTextArea>label {
          color: #f8fafc;
        }

        .hero-card,
        .panel-card,
        .result-card {
          background: rgba(15, 23, 42, 0.88);
          border: 1px solid rgba(148, 163, 184, 0.18);
          border-radius: 24px;
          padding: 28px;
          box-shadow: 0 24px 70px rgba(15, 23, 42, 0.35);
          margin-bottom: 20px;
        }

        .hero-card h1 {
          margin-bottom: 0.4rem;
          font-size: 3rem;
          letter-spacing: -0.04em;
        }

        .hero-description {
          color: #cbd5e1;
          font-size: 1.05rem;
          line-height: 1.75;
          max-width: 720px;
        }

        div[data-testid="metric-container"] {
          background: rgba(15, 23, 42, 0.82) !important;
          border-radius: 18px !important;
          padding: 18px 22px !important;
        }

        .stDataFrame div[role="table"] {
          background: rgba(15, 23, 42, 0.78) !important;
          border-radius: 18px !important;
        }

        .css-1q8dd3e { background-color: rgba(15, 23, 42, 0.05); }
        .css-1aw8r1p { background-color: rgba(255, 255, 255, 0.03); }
        .css-1aumxhk { background-color: rgba(255, 255, 255, 0.03); }
        </style>
        """,
        unsafe_allow_html=True,
    )