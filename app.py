"""from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="say hello in one sentence"
)
print(response.text) """

import streamlit as st
from google import genai
from dotenv import load_dotenv
import os
import pandas as pd
import plotly.express as px
import csv
from datetime import datetime

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="BizInsight 360",
    page_icon="📊",
    layout="wide"
)
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

/* Main Background */

.stApp{
    background: linear-gradient(
    135deg,
    #0f172a 0%,
    #1e293b 30%,
    #312e81 60%,
    #4c1d95 100%);
}

/* Remove Streamlit Header */

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* Hero Banner */

.hero{
    background:linear-gradient(
    135deg,
    #ff6b6b,
    #feca57,
    #48dbfb,
    #5f27cd
    );

    padding:35px;

    border-radius:25px;

    text-align:center;

    color:white;

    margin-bottom:25px;

    box-shadow:0 15px 40px rgba(0,0,0,0.25);
}

.hero h1{
    font-size:48px;
    margin:0;
}

.hero p{
    font-size:20px;
    margin-top:10px;
}

/* Glass Cards */

.card{
    background:rgba(255,255,255,0.12);

    backdrop-filter:blur(18px);

    border:1px solid rgba(255,255,255,0.2);

    padding:25px;

    border-radius:20px;

    color:white;

    box-shadow:0px 8px 25px rgba(0,0,0,0.25);
}

/* Inputs */

.stTextInput input,
.stTextArea textarea{

    background:#ffffff !important;

    color:#000000 !important;

    border-radius:15px !important;

    border:2px solid #cbd5e1 !important;

    padding:12px !important;

    font-size:16px !important;

}

/* Button */

.stButton>button{

    width:100%;

    background:linear-gradient(
    90deg,
    #ff512f,
    #dd2476
    );

    color:white;

    font-size:18px;

    font-weight:bold;

    border:none;

    border-radius:15px;

    padding:15px;

    transition:0.3s;
}

.stButton>button:hover{

    transform:scale(1.03);

    box-shadow:0 10px 25px rgba(255,0,100,0.4);
}

/* Metrics */

[data-testid="metric-container"]{

    background:rgba(255,255,255,0.15);

    border-radius:20px;

    padding:20px;

    box-shadow:0px 8px 25px rgba(0,0,0,0.25);

    color:white;
}

/* Sidebar */

section[data-testid="stSidebar"]{

    background:linear-gradient(
    180deg,
    #111827,
    #1f2937
    );

}

/* Dashboard Title */

.dashboard{

    color:white;

    font-size:32px;

    font-weight:bold;

    margin-top:20px;

}

</style>
""", unsafe_allow_html=True)
# =====================================
# CUSTOM CSS
# =====================================



# =====================================
# LOAD ENV
# =====================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API Key not found in .env file")
    st.stop()

client = genai.Client(api_key=api_key)
category = "Pending"
result = ""
severity = 0

# =====================================
# CSV FILE SETUP
# =====================================

CSV_FILE = "complaints.csv"

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Name",
            "Email",
            "Complaint",
            "Category",
            "Date"
        ])

# =====================================
# SIDEBAR
# =====================================
with st.sidebar:

    st.markdown("""
    <div style="
    background:linear-gradient(
    135deg,
    #FF7A59,
    #FFB26B
    );
    padding:25px;
    border-radius:20px;
    text-align:center;
    color:white;
    ">

    <h2>✨ BizInsight 360</h2>

    <p>
    Turn Complaints Into Growth
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Features")

    st.success("Complaint Classification")
    st.success("Business Analytics")
    st.success("Risk Detection")
    st.success("Executive Insights")
    st.success("Gemini AI")


# =====================================
# HEADER
# =====================================

st.markdown("""
<div class="hero">

<h1>🚀 BizInsight 360</h1>

<p>
AI Powered Complaint Intelligence &
Business Growth Platform
</p>

</div>
""", unsafe_allow_html=True)
# =====================================
# USER INPUTS
# =====================================
st.markdown(
'<div class="card">',
unsafe_allow_html=True
)

st.subheader("📥 Submit Complaint")
name = st.text_input(
    "👤 Full Name"
)

email = st.text_input(
    "📧 Email Address"
)

complaint = st.text_area(
    "📝 Enter Complaint",
    height=180,
    placeholder="Describe your issue here..."
)
st.markdown(
'</div>',
unsafe_allow_html=True
)
# =====================================
# ANALYSIS BUTTON
# =====================================

if st.button("🚀 Analyze Complaint"):

    if not name or not email or not complaint:
        st.warning("Please fill all fields.")
        st.stop()

    prompt = f"""
You are a Business Intelligence System.

Analyze this complaint:

{complaint}

Return ONLY in this format.

🔴 Sentiment:
- One line

📂 Category:
- One category only

⚠ Urgency Score:
- Rate out of 10

🔍 Root Cause:
- Maximum 2 bullet points

📉 Business Impact:
- Maximum 2 bullet points

✅ Recommended Action:
- Maximum 3 bullet points

📊 Executive Insight:
- One short sentence

Keep everything short and concise.
Maximum 120 words total.
"""
    with st.spinner("Analyzing Complaint..."):

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            result = response.text.strip()  





        except Exception as e:

            st.error(f"Error: {e}")
            st.stop()

    st.success("Analysis Completed")

    # =====================================
    # CATEGORY DETECTION
    # =====================================

    result_lower = result.lower()

    if "payroll" in result_lower:
        category = "Payroll"

    elif "delivery" in result_lower:
        category = "Delivery"

    elif "customer support" in result_lower:
        category = "Customer Support"

    elif "product quality" in result_lower:
        category = "Product Quality"

    elif "hr" in result_lower:
        category = "HR"

    elif "technical" in result_lower:
        category = "Technical"

    elif "billing" in result_lower:
        category = "Billing"

    else:
        category = "Others"

    # =====================================
    # SAVE TO CSV
    # =====================================

    with open(
        CSV_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            name,
            email,
            complaint,
            category,
            datetime.now()
        ])
    st.success("analysis completed")
    # =====================================
    # KPIs
    # =====================================
    st.success("Analysis Completed")

# KPI SECTION

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "Complaints",
        "1"
    )

with col2:
    st.metric(
        "Category",
        category
    )

with col3:
        st.metric(
        "AI Model",
        "Gemini"
    )

with col4:
    st.metric(
        "Status",
        "Analyzed"
    )

# =====================================
# DASHBOARD
# =====================================

st.markdown("---")

st.markdown(
"""
<div class="dashboard">
📊 Executive Intelligence Dashboard
</div>
""",
unsafe_allow_html=True
)

try:

    df = pd.read_csv(CSV_FILE)

    total_complaints = len(df)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Complaints",
            total_complaints
        )

    if total_complaints > 0:

        category_counts = (
            df["Category"]
            .value_counts()
            .reset_index()
        )

        category_counts.columns = [
            "Category",
            "Count"
        ]

        category_counts["Percentage"] = (
            category_counts["Count"]
            / total_complaints
        ) * 100

        top_category = (
            category_counts.iloc[0]["Category"]
        )

        with col2:
            st.metric(
                "Most Frequent Issue",
                top_category
            )

        st.subheader(
            "Complaint Distribution"
        )

        pie = px.pie(
            category_counts,
            names="Category",
            values="Count",
            title="Complaint Category Distribution"
        )

        st.plotly_chart(
            pie,
            use_container_width=True
        )

        bar = px.bar(
            category_counts,
            x="Category",
            y="Percentage",
            title="Category Percentage Distribution"
        )

        st.plotly_chart(
            bar,
            use_container_width=True
        )

        st.subheader(
            "📊 Category Breakdown"
        )

        st.dataframe(
            category_counts,
            use_container_width=True
        )

        st.error(
            f"""
⚠ Business Risk Area

Most complaints are related to:

{top_category}

Management should prioritize this area for improvement.
"""
        )

except Exception:
    pass

# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.caption(
    "Built with Streamlit + Gemini AI | BizInsight 360"
)