import streamlit as st
from datetime import date

st.set_page_config(page_title="Late Joiner Penalty Calculator", page_icon="🏥")

st.markdown("""
    <style>
        .main { max-width: 680px; margin: 0 auto; }
        .result-box { padding: 24px; border-radius: 12px; margin-top: 16px; }
        .penalty { background-color: #fff4e6; border: 1px solid #f5c89a; }
        .no-penalty { background-color: #e6f9f3; border: 1px solid #a3e0cc; }
        .big-percent { font-size: 3rem; font-weight: 700; }
        .penalty .big-percent { color: #e07000; }
        .no-penalty .big-percent { color: #00b894; }
    </style>
""", unsafe_allow_html=True)

st.title("Late Joiner Penalty Calculator")
st.caption("Find out whether a late joiner penalty applies to your medical aid, and what percentage it will be.")

st.divider()

# --- STEP 1: DATE OF BIRTH ---
st.subheader("Your date of birth")
st.write("We use this to calculate your current age and determine whether a late joiner penalty could apply to you.")

dob = st.date_input("Date of birth", value=None, max_value=date.today(), format="DD/MM/YYYY")

if dob:
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    if age < 21:
        st.success("✅ Because you are under 21 years old, the late joiner penalty does not apply to you.")
        st.stop()

    st.divider()

    # --- STEP 2: MEDICAL AID HISTORY ---
    st.subheader("Your medical aid history")
    st.write("Have you ever had medical aid cover in South Africa?")

    had_aid = st.radio("Had medical aid?", ["Yes", "No"], index=None, label_visibility="collapsed", horizontal=True)

    if had_aid == "No":
        credible_months = 0
        cert_selections = {}
        proceed = True

    elif had_aid == "Yes":
        st.divider()
        num_memberships = st.number_input("How many different medical aid memberships have you had?", min_value=1, max_value=20, value=1, step=1)

        memberships = []
        cert_selections = {}
        all_filled = True

        for i in range(int(num_memberships)):
            st.markdown(f"**Membership {i + 1}**")
            col1, col2 = st.columns(2)
            with col1:
                start = st.date_input(f"Start date", value=None, max_value=date.today(), format="DD/MM/YYYY", key=f"start_{i}")
            with col2:
                end = st.date_input(f"End date", value=None, max_value=date.today(), format="DD/MM/YYYY", key=f"end_{i}")

            cert = st.radio(
                "Do you have a medical aid certificate for this membership?",
                ["Yes", "No"],
                index=None,
                horizontal=True,
                key=f"cert_{i}"
            )

            if cert is None:
                all_filled = False
            else:
                cert_selections[i] = cert == "Yes"

            if start is None:
                all_filled = False

            memberships.append((start, end, cert))
            st.markdown("---")

        proceed = all_filled

        # Calculate credible months
        credible_months = 0
        if proceed:
            age21_date = date(dob.year + 21, dob.month, dob.day)
            for i, (start, end, cert) in enumerate(memberships):
                end_date = end if end else date.today()
                if start and end_date > start:
                    clipped_start = max(start, age21_date)
                    if clipped_start < end_date:
                        months = (end_date.year - clipped_start.year) * 12 + (end_date.month - clipped_start.month)
                        credible_months += max(0, months)

    else:
        proceed = False

    # --- RESULT ---
    if had_aid and proceed:
        st.divider()
        st.subheader("Your result")

        credible_years = credible_months / 12
        raw_score = age - (35 + credible_years)

        if raw_score <= 0:
            penalty = "0%"
            desc = "Based on your age and years of credible medical aid cover, no late joiner penalty applies to your medical aid premium."
            result_type = "no-penalty"
        elif raw_score < 5:
            penalty = "5%"
            desc = "Your medical aid premium may be loaded by 5% as a late joiner penalty."
            result_type = "penalty"
        elif raw_score < 15:
            penalty = "25%"
            desc = "Your medical aid premium may be loaded by 25% as a late joiner penalty."
            result_type = "penalty"
        elif raw_score < 25:
            penalty = "50%"
            desc = "Your medical aid premium may be loaded by 50% as a late joiner penalty."
            result_type = "penalty"
        else:
            penalty = "75%"
            desc = "Your medical aid premium may be loaded by 75% as a late joiner penalty."
            result_type = "penalty"

        if result_type == "no-penalty":
            st.success(f"### {penalty}\n{desc}")
        else:
            st.warning(f"### {penalty}\n{desc}")

        no_cert = False if had_aid == "No" else any(v == False for v in cert_selections.values())
        if no_cert:
            st.error("⚠️ An affidavit will be required as one or more memberships have no medical aid certificate.")
