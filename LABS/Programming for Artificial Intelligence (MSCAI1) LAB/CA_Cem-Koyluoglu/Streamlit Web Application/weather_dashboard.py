import time

import pandas as pd
import plotly.express as px
import requests
import streamlit as st

# Set up the page title
st.title("Global Weather Data Dashboard")

# Allow users to choose how often the data refreshes
refresh_rate = st.selectbox(
    "Choose how often to refresh (seconds)", options=[1, 2, 5, 10], index=2
)

# Load the cleaned weather data
st.header("Cleaned Weather Data")


@st.cache_data  # Cache the data so it loads faster next time
def load_data():
    """
    Fetch the cleaned weather data from our local Flask API.

    Returns:
        pd.DataFrame: A DataFrame containing the cleaned weather data.
    """
    response = requests.get("http://localhost:5000/data")
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        st.error("Oops! Couldn't load the cleaned data.")
        return pd.DataFrame()


data = load_data()
st.write("Here's the cleaned weather data:")
st.dataframe(data)

# Display live weather updates
st.header("Live Weather Updates")
st.write("Real-time weather data coming through Kafka")


# Function to get live data
def get_live_data():
    """
    Fetch the live weather data from our local Flask API.

    Returns:
        pd.DataFrame: A DataFrame containing the live weather data.
    """
    response = requests.get("http://localhost:5000/live")
    if response.status_code == 200:
        live_data = response.json()
        return pd.DataFrame(live_data)
    else:
        st.error("Hmm, couldn't fetch the live data.")
        return pd.DataFrame()


# Create a placeholder for live data
placeholder = st.empty()

# Keep fetching and displaying live data
while True:
    # Get the latest live data
    live_data = get_live_data()
    with placeholder.container():
        if not live_data.empty:
            st.write("Here are the latest 5 updates:")
            st.dataframe(live_data)

            # Plot real-time temperature changes
            fig = px.line(
                live_data,
                x="last_updated",
                y="temperature",
                title="Real-time Temperature Change",
            )
            st.plotly_chart(fig)
        else:
            st.write("Looks like there's no live data right now.")

    # Wait for the selected interval before refreshing
    time.sleep(refresh_rate)
