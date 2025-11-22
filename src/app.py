import streamlit as st
import json
import pandas as pd

# ───── UI STYLING ──────────────────────────────
RISK_COLORS = {
    "Low": "#3cb371",
    "Medium": "#ffbf00",
    "High": "#ff4d4d"
}

# ───── Simulated Aggregated Result from Agent (for demo) ─────
# Later replace with real function call: run_pipeline(district)
def get_risk_data():
    return {
        "District": "Thanjavur",
        "Overall Risk Level": "Medium",
        "Dimension Risk Levels": {
            "Credit & Financial Behaviour": "Medium",
            "Income Stability": "Medium",
            "Climate & Agricultural Risk": "High",
            "Socio-Economic Vulnerability": "Medium",
            "Infrastructure & Access": "Low",
            "Shock & Event History": "Medium"
        },
        "Key Risk Drivers": [
            "High dependence on paddy agriculture vulnerable to climate shocks",
            "Rising microfinance delinquencies at state level",
            "Recurring floods and droughts impacting income stability"
        ],
        "Safer Borrower Segments": "Borrowers with diversified income sources beyond agriculture (MSME, textiles, handicrafts, salaried).",
        "High-Risk Segments": "Rainfed paddy farmers, seasonal agricultural labourers, and borrowers with multiple informal loans.",
        "Lending Strategy Suggestions": {
            "Ticket Size Guidance": "Small ticket sizes for agriculture-only borrowers; higher for diversified stable incomes.",
            "Product Design Notes": "Seasonal EMI structures + crop insurance + group lending for SHGs with strong track records.",
            "Collection & Operations Notes": "Strengthen early warning and proactive field visits during climate shocks. Digital repayment optional."
        },
        "Summary": "Thanjavur shows a Medium lending risk profile driven mainly by climate vulnerability and agricultural dependence..."
    }

# ───── Streamlit Frontend ──────────────────────
st.set_page_config(page_title="Micro-Lending Risk Dashboard", layout="wide")
st.title("📍 Micro-Lending Risk Assessment Dashboard")

district = st.selectbox("Select District", ["Thanjavur"])
if st.button("Run Assessment"):
    data = get_risk_data()
    
    st.subheader(f"Overall Risk: {data['Overall Risk Level']}")
    st.markdown(
        f"<div style='padding:10px;background:{RISK_COLORS[data['Overall Risk Level']]};color:white;border-radius:8px;font-size:20px;'>"
        f"{data['Overall Risk Level']}"
        "</div>",
        unsafe_allow_html=True
    )
    
    st.markdown("### 🧭 Dimension Risk Levels")
    cols = st.columns(3)
    for i, (dim, level) in enumerate(data["Dimension Risk Levels"].items()):
        with cols[i % 3]:
            st.markdown(
                f"<div style='padding:12px;border-radius:8px;background:{RISK_COLORS[level]};color:white;font-weight:bold;'>"
                f"{dim}<br>{level}</div>",
                unsafe_allow_html=True
            )

    st.markdown("### 🔥 Key Risk Drivers")
    for bullet in data["Key Risk Drivers"]:
        st.write("• " + bullet)

    st.markdown("### 🟢 Safer Borrower Segments")
    st.info(data["Safer Borrower Segments"])

    st.markdown("### 🔺 High-Risk Segments")
    st.warning(data["High-Risk Segments"])

    st.markdown("### 💡 Lending Strategy Suggestions")
    st.write("📌 **Ticket Size Guidance:**", data["Lending Strategy Suggestions"]["Ticket Size Guidance"])
    st.write("📌 **Product Design Notes:**", data["Lending Strategy Suggestions"]["Product Design Notes"])
    st.write("📌 **Collection & Operations Notes:**", data["Lending Strategy Suggestions"]["Collection & Operations Notes"])

    st.markdown("### 📝 Executive Summary")
    st.success(data["Summary"])
