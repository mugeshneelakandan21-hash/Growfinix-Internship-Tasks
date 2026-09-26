import streamlit as st
import pandas as pd
import numpy as np

# Page settings
st.set_page_config(
    page_title="Tour Enquiry Dashboard",
    page_icon="🌍",
    layout="wide"
)

# Title
st.title("🌍 Interactive Tour Enquiry Dashboard")
st.write("Analysis of tour enquiries, destinations, enquiry times, and geographic distribution.")

# Create sample tour enquiry data
np.random.seed(42)

destinations = [
    "Goa",
    "Manali",
    "Ooty",
    "Jaipur",
    "Kerala",
    "Rajasthan"
]

cities = {
    "Goa": (15.4909, 73.8278),
    "Manali": (32.2396, 77.1887),
    "Ooty": (11.4102, 76.6950),
    "Jaipur": (26.9124, 75.7873),
    "Kerala": (9.9312, 76.2673),
    "Rajasthan": (27.0238, 74.2179)
}

enquiry_types = [
    "Family Tour",
    "Adventure",
    "Honeymoon",
    "Solo Travel",
    "Group Tour"
]

rows = []

for i in range(50):
    destination = np.random.choice(destinations)
    latitude, longitude = cities[destination]

    rows.append({
        "Enquiry_ID": f"E{i+1:03d}",
        "Destination": destination,
        "Enquiry_Type": np.random.choice(enquiry_types),
        "Enquiry_Hour": np.random.randint(8, 23),
        "Group_Size": np.random.randint(1, 9),
        "Budget": np.random.randint(10000, 100000),
        "Latitude": latitude + np.random.uniform(-0.08, 0.08),
        "Longitude": longitude + np.random.uniform(-0.08, 0.08)
    })

df = pd.DataFrame(rows)
df.to_csv("tour_enquiries.csv", index=False)

# Sidebar filters
st.sidebar.header("🔎 Filters")

selected_destinations = st.sidebar.multiselect(
    "Select Destination",
    options=sorted(df["Destination"].unique()),
    default=sorted(df["Destination"].unique())
)

filtered_df = df[df["Destination"].isin(selected_destinations)]

# Summary metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Enquiries", len(filtered_df))

with col2:
    st.metric(
        "Popular Destination",
        filtered_df["Destination"].value_counts().idxmax()
        if len(filtered_df) > 0 else "N/A"
    )

with col3:
    st.metric(
        "Average Group Size",
        round(filtered_df["Group_Size"].mean(), 1)
        if len(filtered_df) > 0 else 0
    )

st.divider()

# Popular destinations
st.subheader("📍 Popular Tour Destinations")

destination_counts = (
    filtered_df["Destination"]
    .value_counts()
    .sort_values(ascending=False)
)

st.bar_chart(destination_counts)

# Peak enquiry times
st.subheader("🕐 Peak Enquiry Times")

hour_counts = (
    filtered_df["Enquiry_Hour"]
    .value_counts()
    .sort_index()
)

st.line_chart(hour_counts)

# Geographic distribution
st.subheader("🌍 Geographic Distribution of Enquiries")

if len(filtered_df) > 0:
    st.map(
        filtered_df,
        latitude="Latitude",
        longitude="Longitude",
        size=100
    )
else:
    st.warning("Please select at least one destination.")

# Enquiry type analysis
st.subheader("🎯 Enquiry Types")

type_counts = filtered_df["Enquiry_Type"].value_counts()

st.bar_chart(type_counts)

# Data table
st.subheader("📋 Tour Enquiry Data")

st.dataframe(
    filtered_df,
    width="stretch"
)