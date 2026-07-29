import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Late Joiner Penalty Calculator",
    layout="centered"
)

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.markdown(
    """
    <div class="main-title">
    Late Joiner Penalty Calculator
    </div>

    <div class="subtitle">
    Find out whether a late joiner penalty applies to your medical aid and what percentage it may be.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("Step 1")

dob = st.date_input(
    "Date of Birth",
    min_value=date(1900,1,1),
    max_value=date.today()
)

st.markdown("</div>", unsafe_allow_html=True)
