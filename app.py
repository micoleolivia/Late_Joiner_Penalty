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

# ----------------------------------------------------
# Step 2
# ----------------------------------------------------

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("Step 2")

had_aid = st.radio(
    "Have you ever had medical aid cover in South Africa?",
    ["Yes", "No"],
    horizontal=True
)

if had_aid == "Yes":

    memberships = st.number_input(
        "How many different medical aid memberships have you had?",
        min_value=1,
        max_value=20,
        value=1,
        step=1
    )

else:
    memberships = 0

st.markdown("</div>", unsafe_allow_html=True)
