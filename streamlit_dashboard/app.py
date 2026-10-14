from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

st.markdown("""
<style>
/* PREMIUM PAGE TITLES */
.premium-page-title {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 8px 0 18px 0;
    margin: 0 0 24px 0;
    border-bottom: 2px solid #E5ECF6;
}
.premium-page-title .title-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 52px;
    height: 52px;
    min-width: 52px;
    border-radius: 15px;
    background: linear-gradient(135deg, #163B65, #2878B5);
    color: white;
    font-size: 25px;
    box-shadow: 0 5px 14px rgba(22, 59, 101, 0.18);
}
.premium-page-title .title-text {
    color: #163B65;
    font-size: 30px;
    font-weight: 750;
    letter-spacing: -0.6px;
    line-height: 1.25;
}
.premium-page-title .title-subtitle {
    color: #718096;
    font-size: 13px;
    margin-top: 5px;
    font-weight: 400;
}
@media (max-width: 640px) {
    .premium-page-title .title-text { font-size: 23px; }
    .premium-page-title .title-icon {
        width: 44px; height: 44px; min-width: 44px;
    }
}
</style>
""", unsafe_allow_html=True)


st.set_page_config(
    page_title="Airline Analysis | RUH",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Hide Streamlit's default multipage navigation.
st.markdown("""
<style>
[data-testid="stSidebarNav"] {
    display: none;
}

/* Clean, flat sidebar navigation */
[data-testid="stSidebar"] div[role="radiogroup"] {
    gap: 3px !important;
}

[data-testid="stSidebar"] div[role="radiogroup"] label {
    box-sizing: border-box !important;
    display: flex !important;
    align-items: center !important;
    width: 100% !important;
    min-height: 44px !important;
    background: transparent !important;
    border: none !important;
    border-left: 3px solid transparent !important;
    border-radius: 0 !important;
    padding: 10px 12px !important;
    margin: 0 !important;
    transition: background 0.18s ease;
}

[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background: #EDF3F9 !important;
}

[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    background: #E7F0FA !important;
    border-left-color: #2878C8 !important;
    box-shadow: none !important;
}

[data-testid="stSidebar"] div[role="radiogroup"] label p {
    color: #36536F !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    margin: 0 !important;
}

[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p {
    color: #174A7E !important;
    font-weight: 700 !important;
}

[data-testid="stSidebar"] div[role="radiogroup"] label > div:first-child {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- Theme ----------
NAVY = "#F5F8FC"
PANEL = "#FFFFFF"
BLUE = "#2878C8"
CYAN = "#2878C8"
WHITE = "#172B40"
MUTED = "#61758A"

st.markdown(f"""
<style>
.stApp {{
    background: {NAVY};
    color: {WHITE};
}}
[data-testid="stSidebar"] {{
    background: #FFFFFF;
    border-right: 1px solid #DCE5EF;
}}
h1, h2, h3, p, label {{
    color: {WHITE};
}}
div[data-testid="stMetric"] {{
    background: {PANEL};
    border: 1px solid #DCE5EF;
    border-radius: 14px;
    padding: 18px;
}}
div[data-testid="stMetricLabel"] p {{
    color: {MUTED};
}}
div[data-testid="stMetricValue"] {{
    color: {BLUE};
}}
.stSelectbox label, .stMultiSelect label {{
    color: {WHITE} !important;
}}
a {{
    color: {BLUE} !important;
}}
.hero {{
    background:
        linear-gradient(90deg, rgba(7,20,38,.88), rgba(7,20,38,.25)),
        url("https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=1800&q=85");
    background-size: cover;
    background-position: center;
    border: 1px solid #DCE5EF;
    border-radius: 20px;
    padding: 42px 36px;
    min-height: 260px;
    margin-bottom: 22px;
}}
.eyebrow {{
    color: #BFE4FF;
    letter-spacing: 3px;
    font-size: 12px;
    font-weight: 700;
}}
.hero h1 {{
    color: #FFFFFF !important;
    font-size: 42px;
    margin: 12px 0;
}}
.hero p {{
    color: #FFFFFF !important;
    max-width: 720px;
    font-size: 16px;
}}
.panel {{
    background: {PANEL};
    border: 1px solid #DCE5EF;
    border-radius: 14px;
    padding: 20px;
}}
.small-muted {{
    color: {MUTED};
    font-size: 13px;
}}
.team-card {{
    background: #FFFFFF;
    border: 1px solid #DCE5EF;
    border-top: 4px solid {BLUE};
    border-radius: 16px;
    padding: 22px 12px;
    min-height: 155px;
    text-align: center;
    box-shadow: 0 4px 14px #17324D0D;
}}
.team-name {{
    font-weight: 700;
    color: #17324D;
    margin: 10px 0;
}}
.team-link {{
    display: inline-block;
    background: #EAF3FC;
    color: #2169AB !important;
    border-radius: 8px;
    padding: 8px 10px;
    text-decoration: none !important;
}}
</style>
""", unsafe_allow_html=True)

# ---------- Data ----------
ROOT = Path(__file__).resolve().parent
DATA_CANDIDATES = [
    ROOT.parent / "data" / "flights_RUH.parquet",
    ROOT / "data" / "flights_RUH.parquet",
    ROOT / "flights_RUH.parquet",
]

def load_data(uploaded_file=None):
    if uploaded_file is not None:
        name = uploaded_file.name.lower()
        if name.endswith(".parquet"):
            return pd.read_parquet(uploaded_file)
        if name.endswith((".xlsx", ".xls")):
            return pd.read_excel(uploaded_file)
        if name.endswith(".json"):
            return pd.read_json(uploaded_file)
        return pd.read_csv(uploaded_file)

    for path in DATA_CANDIDATES:
        if path.exists():
            if path.suffix.lower() == ".parquet":
                return pd.read_parquet(path)
            if path.suffix.lower() == ".csv":
                return pd.read_csv(path)
    return None

def find_col(df, words):
    cols = list(df.columns)
    lower = {str(c).lower().replace(" ", "_"): c for c in cols}
    for word in words:
        word = word.lower().replace(" ", "_")
        if word in lower:
            return lower[word]
    for word in words:
        word = word.lower().replace(" ", "_")
        for normalized, original in lower.items():
            if word in normalized:
                return original
    return None

def clean_text(series):
    return series.fillna("Unknown").astype(str)

def chart_layout(fig, height=360):
    fig.update_layout(
        height=height,
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font=dict(color="#172B40"),
        margin=dict(l=15, r=15, t=45, b=15),
        legend=dict(bgcolor="rgba(0,0,0,0)"),
    )
    fig.update_xaxes(gridcolor="#E1E8F0", zerolinecolor="#E1E8F0")
    fig.update_yaxes(gridcolor="#E1E8F0", zerolinecolor="#E1E8F0")
    return fig

def show_bar(df, category, title, limit=12):
    if not category:
        st.info(f"No suitable column was found for {title.lower()}.")
        return
    values = clean_text(df[category]).value_counts().head(limit).reset_index()
    values.columns = [category, "Records"]
    fig = px.bar(values, x="Records", y=category, orientation="h",
                 title=title, color_discrete_sequence=[BLUE], text="Records")
    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(chart_layout(fig), use_container_width=True)

def show_donut(df, category, title):
    if not category:
        st.info(f"No suitable column was found for {title.lower()}.")
        return
    values = clean_text(df[category]).value_counts().head(10).reset_index()
    values.columns = [category, "Records"]
    fig = px.pie(values, names=category, values="Records", hole=.62,
                 title=title, color_discrete_sequence=[BLUE, CYAN, "#7C8CFF",
                 "#F6BD60", "#F28482", "#A8DADC"])
    st.plotly_chart(chart_layout(fig), use_container_width=True)

# ---------- Sidebar ----------
st.sidebar.markdown("""
<div style="padding: 12px 2px 22px 2px; margin-bottom: 18px;">
    <div style="display:flex; align-items:center; gap:11px;">
        <div style="
            min-width:46px;
            height:46px;
            display:flex;
            align-items:center;
            justify-content:center;
            background:linear-gradient(135deg,#174A7E,#2878C8);
            border-radius:14px;
            color:#FFFFFF;
            font-size:24px;
            box-shadow:0 5px 12px rgba(23,74,126,.20);
        ">✈</div>
        <div style="min-width:0;">
            <div style="
                color:#17324D;
                font-size:20px;
                font-weight:800;
                letter-spacing:-.5px;
                line-height:1.25;
                white-space:nowrap;
            ">Airline Analysis</div>
            <div style="
                color:#61758A;
                font-size:9px;
                font-weight:700;
                letter-spacing:1.45px;
                margin-top:6px;
                white-space:nowrap;
            ">FLIGHT DATA INTELLIGENCE</div>
        </div>
    </div>
    <div style="
        height:3px;
        width:54px;
        background:linear-gradient(90deg,#174A7E,#4B97D1);
        border-radius:5px;
        margin-top:19px;
    "></div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div style="
    font-size:11px;
    font-weight:800;
    letter-spacing:2px;
    color:#61758A;
    margin: 0 0 12px 2px;
">EXPLORE DASHBOARD</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Choose a page",
    [
        "Overview",
        "Flight Operations",
        "Airport Insights",
        "Airline Performance",
    ],
    label_visibility="collapsed",
    key="main_navigation",
)

page = {
    "Overview": "Overview",
    "Flight Operations": "Flight_Operations",
    "Airport Insights": "Airport_Insights",
    "Airline Performance": "Airline_Performance",
}[page]
st.sidebar.markdown("---")
st.sidebar.markdown("### 📂 Flight dataset")
uploaded = st.sidebar.file_uploader(
    "Upload CSV, Parquet, Excel or JSON",
    type=["csv", "parquet", "xlsx", "xls", "json"],
)

try:
    df = load_data(uploaded)
except Exception as exc:
    df = None
    st.sidebar.error(f"Could not read the dataset: {exc}")

if df is None:
    st.markdown("""
    <div class="hero">
      <div class="eyebrow">AVIATION INTELLIGENCE</div>
      <h1>Airline Analysis ✈️</h1>
      <p>Transforming flight movement data into valuable insights.
      Explore airport operations, discover performance patterns,
      and support data-driven decision-making.</p>
    </div>
    """, unsafe_allow_html=True)
    st.warning(
        "The flight dataset was not found. Place `flights_RUH.parquet` "
        "in the project's `data` folder, or upload your dataset using the sidebar."
    )
    st.stop()

df.columns = [str(c).strip() for c in df.columns]
df = df.dropna(how="all")
if df.empty:
    st.error("The dataset is empty.")
    st.stop()

# Try to identify common flight-data columns
airline_col = find_col(df, ["airline", "airline_name", "carrier"])
origin_col = find_col(df, ["origin_airport_iata", "origin_airport", "origin", "departure_airport"])
destination_col = find_col(df, ["destination_airport_iata", "destination_airport", "destination", "arrival_airport"])
status_col = find_col(df, ["status", "flight_status"])
type_col = find_col(df, ["flight_type", "type"])
terminal_col = find_col(df, ["terminal", "movement_terminal"])
date_col = find_col(df, ["scheduled_departure", "scheduled_time", "flight_date", "date", "departure_time", "timestamp"])
flight_col = find_col(df, ["flight_number", "flight_no", "flight"])
cargo_col = find_col(df, ["cargo", "cargo_weight", "freight"])

# Convert likely date/time field
if date_col:
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

# Shared filters
st.sidebar.markdown("---")
st.sidebar.markdown("### 🎛️ Filters")
filtered = df.copy()

if airline_col:
    options = sorted(clean_text(df[airline_col]).unique().tolist())
    selected = st.sidebar.multiselect("Airline", options, default=[])
    if selected:
        filtered = filtered[clean_text(filtered[airline_col]).isin(selected)]

if status_col:
    options = sorted(clean_text(filtered[status_col]).unique().tolist())
    selected = st.sidebar.multiselect("Flight status", options, default=[])
    if selected:
        filtered = filtered[clean_text(filtered[status_col]).isin(selected)]

if origin_col:
    options = sorted(clean_text(filtered[origin_col]).unique().tolist())
    selected = st.sidebar.multiselect("Origin airport", options, default=[])
    if selected:
        filtered = filtered[clean_text(filtered[origin_col]).isin(selected)]

# ---------- Header ----------
if page == "Overview":
    st.markdown("""
    <div class="hero">
      <div class="eyebrow">AVIATION INTELLIGENCE</div>
      <h1>Airline Analysis ✈️</h1>
      <p>Transforming flight movement data into valuable insights.
      Explore airport operations, discover performance patterns,
      and support data-driven decision-making.</p>
      <p>📍 King Khalid International Airport (RUH), Riyadh, Saudi Arabia</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f'<div class="eyebrow">AIRLINE ANALYTICS / RUH</div>', unsafe_allow_html=True)
    st.title(page.replace("_", " "))
    st.caption("Explore the flight dataset using the interactive filters in the sidebar.")

# ---------- KPI row ----------
total_records = len(filtered)
airline_count = filtered[airline_col].nunique() if airline_col else None
origin_count = filtered[origin_col].nunique() if origin_col else None
destination_count = filtered[destination_col].nunique() if destination_col else None

c1, c2, c3, c4 = st.columns(4)
c1.metric("Flight Records", f"{total_records:,}")
c2.metric("Airlines", f"{airline_count:,}" if airline_count is not None else "N/A")
c3.metric("Origin Airports", f"{origin_count:,}" if origin_count is not None else "N/A")
c4.metric("Destinations", f"{destination_count:,}" if destination_count is not None else "N/A")

st.markdown("---")

# ---------- Overview ----------
if page == "Overview":
    left, right = st.columns(2)
    with left:
        show_bar(filtered, airline_col, "Flight Records by Airline")
    with right:
        show_donut(filtered, status_col, "Flight Status Distribution")

    if date_col and filtered[date_col].notna().any():
        trend = filtered.dropna(subset=[date_col]).copy()
        trend["Date"] = trend[date_col].dt.date
        trend = trend.groupby("Date").size().reset_index(name="Flight Records")
        fig = px.line(trend, x="Date", y="Flight Records",
                      title="Flight Activity Over Time",
                      markers=True, color_discrete_sequence=[CYAN])
        st.plotly_chart(chart_layout(fig), use_container_width=True)

    st.subheader("Dataset Preview")
    st.dataframe(filtered.head(100), use_container_width=True, hide_index=True)

# ---------- Flight Operations ----------
elif page == "Flight_Operations":
    left, right = st.columns(2)
    with left:
        show_donut(filtered, status_col, "Flight Status Breakdown")
    with right:
        if type_col:
            values = clean_text(filtered[type_col]).value_counts().head(10).reset_index()
            values.columns = [type_col, "Records"]
            fig = px.pie(
                values,
                names=type_col,
                values="Records",
                hole=0.62,
                title="Flight Type Breakdown",
                color_discrete_sequence=[
                    "#174A7E", "#2169AB", "#2878C8",
                    "#365F91", "#153653", "#4B97D1"
                ],
            )
            st.plotly_chart(chart_layout(fig), use_container_width=True)
        else:
            st.info("No suitable column was found for flight type breakdown.")

    if date_col and filtered[date_col].notna().any():
        timed = filtered.dropna(subset=[date_col]).copy()
        timed["Hour"] = timed[date_col].dt.hour
        hourly = timed.groupby("Hour").size().reset_index(name="Flight Records")
        fig = px.bar(hourly, x="Hour", y="Flight Records",
                     title="Flight Activity by Hour",
                     color_discrete_sequence=[BLUE])
        st.plotly_chart(chart_layout(fig), use_container_width=True)

    st.subheader("Flight Operations Data")
    st.dataframe(filtered, use_container_width=True, hide_index=True)

# ---------- Airport Insights ----------
elif page == "Airport_Insights":
    left, right = st.columns(2)

    # Airports with fewer than 5 flights (SQL equivalent)
    with left:
        destination_name_col = find_col(
            filtered, ["destination_airport_name"]
        )

        if destination_name_col:
            rare_destinations = (
                filtered.dropna(subset=[destination_name_col])
                .groupby(destination_name_col)
                .size()
                .reset_index(name="count")
            )

            rare_destinations = (
                rare_destinations[rare_destinations["count"] < 5]
                .sort_values("count", ascending=True)
            )

            if not rare_destinations.empty:
                fig = px.bar(
                    rare_destinations,
                    x="count",
                    y=destination_name_col,
                    orientation="h",
                    title="Destination Airports with Fewer Than 5 Flights",
                    labels={
                        "count": "Flight Count",
                        destination_name_col: "Destination Airport",
                    },
                    color_discrete_sequence=["#2878C8"],
                    text="count",
                )
                fig.update_layout(
                    yaxis={"categoryorder": "array",
                           "categoryarray": rare_destinations[
                               destination_name_col
                           ].tolist()},
                    showlegend=False,
                )
                st.plotly_chart(
                    chart_layout(fig, max(360, len(rare_destinations) * 28)),
                    use_container_width=True,
                )
            else:
                st.info("No destination airports have fewer than 5 flights.")
        else:
            st.info("Column destination_airport_name was not found.")

    with right:
        show_bar(filtered, destination_col, "Top Destination Airports")

    if origin_col and destination_col:
        routes = filtered.copy()
        routes["Route"] = clean_text(routes[origin_col]) + " → " + clean_text(routes[destination_col])
        route_counts = routes["Route"].value_counts().head(15).reset_index()
        route_counts.columns = ["Route", "Flight Records"]
        fig = px.bar(route_counts, x="Flight Records", y="Route",
                     orientation="h", title="Most Frequent Routes",
                     color_discrete_sequence=[CYAN], text="Flight Records")
        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(chart_layout(fig, 420), use_container_width=True)

    if terminal_col:
        show_donut(filtered, terminal_col, "Terminal Distribution")

# ---------- Airline Performance ----------
elif page == "Airline_Performance":
    if airline_col:
        performance = filtered.copy()
        performance[airline_col] = clean_text(performance[airline_col])
        summary = performance.groupby(airline_col).size().reset_index(name="Flight Records")
        summary = summary.sort_values("Flight Records", ascending=False)
        fig = px.bar(summary.head(20), x=airline_col, y="Flight Records",
                     title="Airline Activity Comparison",
                     color="Flight Records",
                     color_continuous_scale=["#24507A", BLUE, CYAN],
                     text="Flight Records")
        fig.update_layout(xaxis_tickangle=-35, coloraxis_showscale=False)
        st.plotly_chart(chart_layout(fig, 420), use_container_width=True)
        st.subheader("Airline Summary")
        st.dataframe(summary, use_container_width=True, hide_index=True)
        st.download_button(
            "⬇️ Download Airline Summary CSV",
            data=summary.to_csv(index=False).encode("utf-8"),
            file_name="airline_performance_summary.csv",
            mime="text/csv",
        )
    else:
        st.info("An airline column could not be detected. Review the dataset columns below.")
        st.dataframe(filtered.head(100), use_container_width=True, hide_index=True)


# ---------- Team & Footer ----------
st.markdown("---")
st.markdown("## 👩🏻‍💻 Meet the Team")
st.caption("Training Camp by SDA & Le Wagon")
team = [
    ("MARIAM MUBARAK", "https://www.linkedin.com/in/maryam-mubarak-548b42296/"),
    ("Razan Alzahrani", "https://www.linkedin.com/in/razan-alzahrani-89513620b/"),
    ("Elham Alansari", "https://www.linkedin.com/in/elham-alansari-1a1344246/"),
    ("Nada Almetairi", "https://www.linkedin.com/in/nada-almetairi/"),
]
cols = st.columns(4)
for col, (name, url) in zip(cols, team):
    with col:
        st.markdown(
            f'<div class="team-card"><div style="font-size:26px">👩🏻‍💻</div>'
            f'<div class="team-name">{name}</div>'
            f'<a class="team-link" href="{url}" target="_blank">View LinkedIn ↗</a></div>',
            unsafe_allow_html=True,
        )
st.caption("✈️ Airline Analysis · SDA & Le Wagon")


st.markdown("""
<style>
/* FIX_EXPLORE_DASHBOARD_RADIO_CIRCLES */
div[data-testid="stRadio"] label > div:first-child {
    display: none !important;
}
div[data-testid="stRadio"] label {
    gap: 0 !important;
}
</style>
""", unsafe_allow_html=True)
