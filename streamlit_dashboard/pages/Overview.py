
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.markdown("""
<style>
.block-container {padding-top: 1.5rem; padding-bottom: 3rem;}
.hero {
    background: linear-gradient(120deg, #0B1F3A 0%, #153E75 60%, #247BA0 100%);
    padding: 34px;
    border-radius: 22px;
    color: white;
    margin-bottom: 22px;
}
.hero h1 {color: white !important; font-size: 2.5rem !important;}
.hero p {color: #E6F1FF !important; font-size: 1.05rem;}
.section {
    background: white;
    padding: 22px;
    border: 1px solid #E5ECF5;
    border-radius: 18px;
    margin: 12px 0;
}
.member {
    background: white;
    padding: 17px;
    border: 1px solid #E5ECF5;
    border-radius: 14px;
    min-height: 105px;
}
.small-label {color: #60748B; font-size: 0.85rem;}
</style>
""", unsafe_allow_html=True)

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "flights_RUH.parquet"

left, right = st.columns([1.2, 0.8], gap="large", vertical_alignment="center")

with left:
    st.markdown("""
    <div class="hero">
        <div style="font-size:14px; letter-spacing:2px; font-weight:700;">
            ✈️ AIRPORT DATA INTELLIGENCE
        </div>
        <h1>Airline Analysis</h1>
        <p>
        Transforming flight movement data into valuable insights.
        Explore airport operations, discover performance patterns,
        and support data-driven decision-making.
        </p>
        <p><b>📍 King Khalid International Airport (RUH)</b><br>
        Riyadh, Saudi Arabia</p>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.image(
        "https://images.unsplash.com/photo-1436491865332-7a61a109cc05"
        "?auto=format&fit=crop&w=1200&q=85",
        caption="Aviation • Operations • Insights",
        use_container_width=True
    )

st.markdown("""
<div class="section">
    <h3>🎯 About the Project</h3>
    <p>
    This project explores airline and airport data to understand flight
    activity, review operational patterns, compare airline performance,
    and present meaningful findings through interactive visualizations.
    </p>
    <p><b>Training program:</b> SDA &amp; Le Wagon</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## 📊 Dashboard Highlights")
st.caption("Explore the pages from the sidebar to investigate each area in detail.")

col1, col2, col3 = st.columns(3)
col1.markdown(
    '<div class="member">🛫 <b>Flight Operations</b><br>'
    '<span class="small-label">Flight activity and status</span></div>',
    unsafe_allow_html=True
)
col2.markdown(
    '<div class="member">🛬 <b>Airport Insights</b><br>'
    '<span class="small-label">Airport movement patterns</span></div>',
    unsafe_allow_html=True
)
col3.markdown(
    '<div class="member">📈 <b>Airline Performance</b><br>'
    '<span class="small-label">Airline comparisons</span></div>',
    unsafe_allow_html=True
)

# Quick overview charts, loaded only when the dataset is available.
if DATA_PATH.exists():
    try:
        df = pd.read_parquet(DATA_PATH)
        df.columns = df.columns.str.strip()

        st.markdown("## ✨ At a Glance")

        total = len(df)
        airlines = (
            df["airline.name"].nunique()
            if "airline.name" in df.columns else 0
        )
        origins = (
            df["origin_airport_name"].nunique()
            if "origin_airport_name" in df.columns else 0
        )
        destinations = (
            df["destination_airport_name"].nunique()
            if "destination_airport_name" in df.columns else 0
        )

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total Flight Records", f"{total:,}")
        m2.metric("Airlines", f"{airlines:,}")
        m3.metric("Origin Airports", f"{origins:,}")
        m4.metric("Destination Airports", f"{destinations:,}")

        chart1, chart2 = st.columns(2, gap="large")

        if "airline.name" in df.columns:
            with chart1:
                airline_counts = (
                    df["airline.name"].dropna().astype(str)
                    .value_counts().head(10).sort_values()
                )
                fig = px.bar(
                    x=airline_counts.values,
                    y=airline_counts.index,
                    orientation="h",
                    title="Top 10 Airlines by Flight Records",
                    labels={"x": "Flight Records", "y": "Airline"},
                    color=airline_counts.values,
                    color_continuous_scale=["#A8DADC", "#247BA0", "#153E75"],
                )
                fig.update_layout(
                    template="plotly_white",
                    showlegend=False,
                    coloraxis_showscale=False,
                    margin=dict(l=10, r=10, t=55, b=10),
                )
                st.plotly_chart(fig, use_container_width=True)

        if "status" in df.columns:
            with chart2:
                status_counts = df["status"].fillna("Unknown").astype(str).value_counts()
                fig = px.pie(
                    names=status_counts.index,
                    values=status_counts.values,
                    title="Flight Status Distribution",
                    hole=0.58,
                    color_discrete_sequence=[
                        "#153E75", "#247BA0", "#70C1B3",
                        "#F4A261", "#A8DADC", "#7C83FD"
                    ],
                )
                fig.update_layout(
                    template="plotly_white",
                    margin=dict(l=10, r=10, t=55, b=10),
                    legend_title_text="Status",
                )
                st.plotly_chart(fig, use_container_width=True)

    except Exception as exc:
        st.warning(
            "The overview page is ready, but the quick charts could not "
            f"be loaded from the dataset: {exc}"
        )
else:
    st.info(
        "The overview page is ready. Add the dataset at "
        "`data/flights_RUH.parquet` to display the summary charts."
    )

st.markdown("---")
st.markdown("## 👩🏻‍💻 Meet the Developers")
st.caption("Created as part of the SDA & Le Wagon training program.")

developers = [
    ("Mariam Mubarak", "https://www.linkedin.com/in/maryam-mubarak-548b42296/"),
    ("Razan Alzahrani", "https://www.linkedin.com/in/razan-alzahrani-89513620b/"),
    ("Elham Alansari", "https://www.linkedin.com/in/elham-alansari-1a1344246/"),
    ("Nada Almetairi", "https://www.linkedin.com/in/nada-almetairi/"),
]

cols = st.columns(4)
for col, (name, url) in zip(cols, developers):
    with col:
        st.markdown(
            f'<div class="member">👩🏻‍💻<br><b>{name}</b><br>'
            f'<a href="{url}" target="_blank" '
            f'style="color:#247BA0; text-decoration:none;">'
            f'LinkedIn ↗</a></div>',
            unsafe_allow_html=True
        )

st.markdown("")
st.markdown(
    '<div style="text-align:center; color:#748399; padding:14px;">'
    '✈️ Airline Analysis | King Khalid International Airport (RUH)'
    '</div>',
    unsafe_allow_html=True
)
