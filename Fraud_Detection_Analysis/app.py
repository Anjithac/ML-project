
import streamlit as st
import pandas as pd
import joblib

# ==================================================
# PAGE CONFIGURATION
# ==================================================
st.set_page_config(
    page_title="FraudGuard | Fraud Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# CUSTOM CSS - DASHBOARD + VISIBLE SIDEBAR
# ==================================================
st.markdown("""
<style>
/* Main background */
.stApp {
    background: linear-gradient(135deg, #07111f, #10213a);
    color: #f1f5f9;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Main headings */
h1, h2, h3, p, label {
    color: #f1f5f9;
}

/* Hero banner */
.hero {
    background: linear-gradient(120deg, #14365b, #17658a);
    border: 1px solid #32648a;
    border-radius: 20px;
    padding: 32px;
    margin-bottom: 25px;
}

.hero h1 {
    color: #ffffff !important;
    font-size: 36px;
    margin-bottom: 12px;
}

.hero p {
    color: #e0f2fe !important;
    font-size: 16px;
}

/* Dashboard cards */
.card {
    background: #172840;
    border: 1px solid #304967;
    border-radius: 16px;
    padding: 22px;
    min-height: 125px;
    margin-bottom: 15px;
}

.card-label {
    color: #b8cee5 !important;
    font-size: 13px;
    letter-spacing: 1px;
}

.card-value {
    color: #ffffff !important;
    font-size: 25px;
    font-weight: 700;
    margin-top: 12px;
}

/* Form container */
[data-testid="stVerticalBlockBorderWrapper"] {
    border-color: #304967;
    border-radius: 16px;
}

/* Input labels */
.stNumberInput label,
.stSelectbox label {
    color: #dbeafe !important;
    font-weight: 600;
}

/* Buttons */
div.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #1677d2, #0891b2);
    color: #ffffff !important;
    border: none;
    border-radius: 10px;
    padding: 13px;
    font-weight: 700;
    transition: 0.2s;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #1d8af0, #06b6d4);
    border: 1px solid #bfdbfe;
}

/* Metrics */
[data-testid="stMetric"] {
    background: #172840;
    border: 1px solid #304967;
    border-radius: 14px;
    padding: 18px;
}

[data-testid="stMetricLabel"] {
    color: #bfdbfe !important;
}

[data-testid="stMetricValue"] {
    color: #ffffff !important;
}

/* Sidebar background */
[data-testid="stSidebar"] {
    background-color: #edf4fc !important;
    border-right: 1px solid #cbd9e8;
}

/* Sidebar text - navy blue */
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"],
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {
    color: #102a4c !important;
}

/* Sidebar navigation text */
[data-testid="stSidebar"] [role="radiogroup"] label,
[data-testid="stSidebar"] [role="radiogroup"] label p,
[data-testid="stSidebar"] [role="radiogroup"] label span {
    color: #102a4c !important;
}

/* Sidebar separators */
[data-testid="stSidebar"] hr {
    border-color: #c7d5e5;
}

/* Sidebar radio controls */
[data-testid="stSidebar"] [role="radiogroup"] {
    gap: 12px;
}

/* Help and footer text */
.stCaption, [data-testid="stCaptionContainer"] p {
    color: #a9bdd3;
}

/* Divider */
hr {
    border-color: #304967;
}

/* Mobile-friendly layout */
@media (max-width: 768px) {
    .hero {
        padding: 22px;
    }

    .hero h1 {
        font-size: 27px;
    }

    .card-value {
        font-size: 20px;
    }
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# LOAD TRAINED MODEL
# ==================================================
@st.cache_resource
def load_model():
    return joblib.load("fraud_detection_model.pkl")

try:
    model = load_model()
except Exception as e:
    st.error("Unable to load the saved model.")
    st.write("Check that fraud_detection_model.pkl is in your project folder.")
    st.code(str(e))
    st.stop()

# ==================================================
# SIDEBAR
# ==================================================
with st.sidebar:
    st.markdown("# 🛡️ FraudGuard")
    st.markdown("### Transaction Security")
    st.caption("AI-powered fraud risk screening")

    st.markdown("---")

    page = st.radio(
        "NAVIGATION",
        ["🏠 Dashboard", "📘 About Project"]
    )

    st.markdown("---")
    st.markdown("### 🔐 System Information")
    st.caption("Model: Loaded")
    st.caption("Framework: Scikit-learn")
    st.caption("Interface: Streamlit")

    st.markdown("---")
    st.caption("Educational project")
    st.caption("Predictions require validation")

# ==================================================
# ABOUT PAGE
# ==================================================
if page == "📘 About Project":
    st.markdown("""
    <div class="hero">
        <h1>📘 About FraudGuard</h1>
        <p>An intelligent machine learning application for
        estimating financial transaction fraud risk.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🧠 Project Overview")

    st.write(
        "FraudGuard uses a trained machine learning model to "
        "classify a transaction based on the transaction features "
        "provided by the user."
    )

    st.markdown("## 🛠️ Technologies Used")
    t1, t2, t3 = st.columns(3)

    with t1:
        st.info("🐍 Python")
    with t2:
        st.info("📊 Pandas")
    with t3:
        st.info("🤖 Scikit-learn")

    st.warning(
        "This application is for demonstration purposes. "
        "A model prediction is not proof of fraud and should "
        "not be used alone to block real transactions."
    )
    st.stop()

# ==================================================
# DASHBOARD HEADER
# ==================================================
st.markdown("""
<div class="hero">
    <h1>🛡️ Fraud Detection Dashboard</h1>
    <p>Intelligent transaction screening powered by machine learning.</p>
    <p>Enter transaction details below to estimate fraud risk.</p>
</div>
""", unsafe_allow_html=True)

# ==================================================
# TOP DASHBOARD CARDS
# ==================================================
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
        <div class="card-label">🤖 ANALYSIS ENGINE</div>
        <div class="card-value">ML Model</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <div class="card-label">🔍 SCREENING MODE</div>
        <div class="card-value">Transaction Analysis</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        <div class="card-label">📊 PREDICTION OUTPUT</div>
        <div class="card-value">Fraud Risk Estimate</div>
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# TRANSACTION INPUT FORM
# ==================================================
st.markdown("## 💳 Transaction Details")
st.caption("Enter the transaction values for analysis.")

with st.container(border=True):
    left, right = st.columns(2)

    with left:
        step = st.number_input(
            "⏱️ Transaction Step",
            min_value=1,
            value=5
        )

        transaction_type = st.selectbox(
            "🔄 Transaction Type",
            ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"]
        )

        amount = st.number_input(
            "💰 Transaction Amount",
            min_value=0.0,
            value=999.88,
            step=100.0
        )

        oldbalanceOrg = st.number_input(
            "👤 Sender's Old Balance",
            min_value=0.0,
            value=5000.10,
            step=100.0
        )

    with right:
        newbalanceOrig = st.number_input(
            "👤 Sender's New Balance",
            min_value=0.0,
            value=4000.00,
            step=100.0
        )

        oldbalanceDest = st.number_input(
            "🏦 Receiver's Old Balance",
            min_value=0.0,
            value=0.11,
            step=100.0
        )

        newbalanceDest = st.number_input(
            "🏦 Receiver's New Balance",
            min_value=0.0,
            value=1000.00,
            step=100.0
        )

    st.markdown("---")
    analyze = st.button("🔍 Analyze Transaction Risk")

# ==================================================
# MODEL PREDICTION
# ==================================================
if analyze:
    transaction = pd.DataFrame([{
        "step": step,
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    try:
        prediction = int(model.predict(transaction)[0])

        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(transaction)[0]
            classes = list(model.classes_)
            fraud_index = classes.index(1)
            probability = float(probabilities[fraud_index])
        else:
            probability = None

        st.markdown("---")
        st.markdown("## 📈 Transaction Analysis Results")

        result_col, amount_col = st.columns(2)

        with result_col:
            if prediction == 1:
                st.error("🚨 Model Classification: FRAUD")
            else:
                st.success("✅ Model Classification: NOT FRAUD")

        with amount_col:
            st.metric("Transaction Amount", f"{amount:,.2f}")

        if probability is not None:
            p1, p2 = st.columns([2, 1])

            with p1:
                st.markdown("### Estimated Fraud Probability")
                st.progress(max(0.0, min(1.0, probability)))
                st.metric("Fraud Risk Estimate", f"{probability:.2%}")

            with p2:
                st.markdown("### Transaction Type")
                st.markdown(f"**{transaction_type}**")
                st.markdown(f"**Step:** {step}")

            chart = pd.DataFrame({
                "Category": ["Estimated fraud probability",
                             "Remaining probability"],
                "Probability": [probability, 1.0 - probability]
            })

            st.markdown("### 📊 Probability Overview")
            st.bar_chart(
                chart.set_index("Category"),
                horizontal=True
            )

        st.markdown("### 🧾 Transaction Summary")
        summary = pd.DataFrame({
            "Feature": [
                "Transaction Type",
                "Transaction Amount",
                "Sender's Old Balance",
                "Sender's New Balance",
                "Receiver's Old Balance",
                "Receiver's New Balance"
            ],
            "Value": [
                transaction_type,
                f"{amount:,.2f}",
                f"{oldbalanceOrg:,.2f}",
                f"{newbalanceOrig:,.2f}",
                f"{oldbalanceDest:,.2f}",
                f"{newbalanceDest:,.2f}"
            ]
        })

        st.dataframe(summary, use_container_width=True, hide_index=True)

        st.info(
            "This is a machine learning estimate, not a confirmed "
            "fraud decision. Review model performance and select an "
            "appropriate classification threshold using validation data."
        )

    except Exception as e:
        st.error("Prediction failed.")
        st.write(
            "Check that the saved model expects the same feature "
            "names and data types as the transaction inputs."
        )
        st.code(str(e))

# ==================================================
# FOOTER
# ==================================================
st.markdown("---")
st.caption(
    "🛡️ FraudGuard | AI Fraud Detection Project | "
    "For educational and demonstration use"
)
