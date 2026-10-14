import streamlit as st

st.set_page_config(
    page_title="Airline Analysis",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
.stApp { background: #F5F8FC; }
.block-container { max-width: 1250px; padding-top: 2rem; }
.hero {
    background: linear-gradient(120deg, #102A43, #176B87);
    padding: 40px;
    border-radius: 20px;
    color: white;
}
.hero h1 { color: white; font-size: 42px; }
.hero p { color: #E4F1F7; line-height: 1.8; font-size: 16px; }
.section-title {
    font-size: 26px;
    font-weight: 700;
    color: #102A43;
    margin-top: 25px;
    margin-bottom: 12px;
}
.info-card {
    background: white;
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #E1E8F0;
    min-height: 155px;
}
.info-card h3 { color: #176B87; font-size: 17px; }
.info-card p { color: #526579; font-size: 14px; }
.team-card {
    background: white;
    border: 1px solid #E1E8F0;
    border-radius: 15px;
    padding: 20px 10px;
    text-align: center;
    min-height: 125px;
}
.team-card h4 { color: #102A43; font-size: 15px; }
.footer {
    text-align: center;
    color: #627D98;
    padding: 25px 0;
    font-size: 12px;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## ✈️ Airline Analysis")
    st.caption("FLIGHT OPERATIONS INTELLIGENCE")
    st.divider()
    st.write("**Project Navigation**")
    st.caption("Choose a page from the sidebar to explore the project.")
    st.divider()
    st.caption("SDA × Le Wagon")
    st.caption("Data Engineering Bootcamp")

st.markdown("""
<div class="hero" style="
    position: relative;
    overflow: hidden;
    background:
        linear-gradient(90deg,
            rgba(8, 30, 58, 0.97) 0%,
            rgba(12, 57, 91, 0.88) 48%,
            rgba(12, 57, 91, 0.18) 100%),
        url('https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=1800&q=90');
    background-size: cover;
    background-position: center;
    min-height: 340px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 42px;
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 15px 40px rgba(16,42,67,0.18);
">
    <p style="
        color: #79E2E8;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 2.5px;
        margin-bottom: 12px;
    ">
        SDA × LE WAGON | DATA ENGINEERING BOOTCAMP
    </p>
    <h1 style="
        color: white;
        font-size: clamp(32px, 4vw, 48px);
        margin: 0 0 14px 0;
        text-shadow: 0 2px 15px rgba(0,0,0,0.2);
    ">
        Airline Analysis
    </h1>
    <p style="
        color: #F0F7FF;
        font-size: 16px;
        line-height: 1.9;
        max-width: 620px;
        margin-bottom: 18px;
    ">
        Turning flight movement data into meaningful insights.
        Explore airport operations, discover performance patterns,
        and support data-driven decision-making.
    </p>
    <p style="
        color: #D6F4F5;
        font-size: 14px;
        line-height: 1.8;
        margin-bottom: 0;
    ">
        📍 King Khalid International Airport (RUH)<br>
        Riyadh, Saudi Arabia
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">About the Project</div>',
    unsafe_allow_html=True,
)

st.write("""
Airline Analysis is an end-to-end data engineering project developed
as part of the SDA × Le Wagon Data Engineering Bootcamp.

The project focuses on processing and analyzing flight movement data
associated with King Khalid International Airport in Riyadh, Saudi Arabia.

The pipeline follows the Medallion Architecture, organizing data into
Bronze, Silver, and Gold layers to support data preparation, quality
improvement, and analytical reporting.

The objective is to transform aviation data into useful insights that
help users understand airport activity and operational patterns.
""")

st.markdown(
    '<div class="section-title">Explore the Dataset</div>',
    unsafe_allow_html=True,
)

c1, c2, c3, c4 = st.columns(4)

cards = [
    (c1, "📍 Airport", "King Khalid International Airport", "Airport code: RUH"),
    (c2, "🌍 Location", "Riyadh, Saudi Arabia", "Airport flight movements"),
    (c3, "🗂️ Dataset", "Flight Movement Data", "Prepared for analysis"),
    (c4, "⚙️ Architecture", "Medallion Architecture", "Bronze → Silver → Gold"),
]

for col, title, value, description in cards:
    with col:
        st.markdown(f"""
        <div class="info-card">
            <h3>{title}</h3>
            <p><strong>{value}</strong></p>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">Our Data Pipeline</div>',
    unsafe_allow_html=True,
)

b1, b2, b3 = st.columns(3)

with b1:
    st.markdown("### 🥉 Bronze")
    st.write("Raw data ingestion and initial storage.")

with b2:
    st.markdown("### 🥈 Silver")
    st.write("Data cleaning, validation, and transformation.")

with b3:
    st.markdown("### 🥇 Gold")
    st.write("Analytics-ready datasets for reporting and insights.")

st.info(
    "The dashboard is currently a presentation interface. "
    "Operational KPIs and charts will be connected after the Gold Layer "
    "tables and their schemas are available."
)

st.markdown(
    '<div class="section-title">Meet the Team</div>',
    unsafe_allow_html=True,
)

st.write("Developed collaboratively as part of the SDA × Le Wagon Bootcamp.")

team = [
    ("Maryam Mubarak", "ADD_MARYAM_LINKEDIN_URL"),
    ("Razan Alzahrani", "ADD_RAZAN_LINKEDIN_URL"),
    ("Elham Alansari", "ADD_ELHAM_LINKEDIN_URL"),
    ("Nada Almutairi", "ADD_NADA_LINKEDIN_URL"),
]

team_cols = st.columns(4)

for col, (name, url) in zip(team_cols, team):
    with col:
        st.markdown(f"""
        <div class="team-card">
            <div style="font-size:28px;">👩🏻‍💻</div>
            <h4>{name}</h4>
            <p>Data Engineering Project</p>
        </div>
        """, unsafe_allow_html=True)

        if url.startswith("https://www.linkedin.com/"):
            st.markdown(f"[LinkedIn profile]({url})")
        else:
            st.caption("LinkedIn link to be added")

st.markdown("---")
st.markdown("""
<div class="footer">
    Airline Analysis · SDA × Le Wagon Data Engineering Bootcamp<br>
    Built with Python and Streamlit
</div>
""", unsafe_allow_html=True)
