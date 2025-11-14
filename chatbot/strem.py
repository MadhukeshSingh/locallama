import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration for a wide layout and a custom title/icon
st.set_page_config(layout="wide", page_title="Awesome Streamlit App", page_icon=":rocket:")

st.title("🚀 My Awesome Streamlit Dashboard")
st.markdown("This is an example of a well-structured Streamlit UI.")

# Sidebar for controls
with st.sidebar:
    st.header("App Controls")
    selected_option = st.selectbox(
        "Choose a data view:",
        ("Overview", "Detailed Analysis", "Settings")
    )
    data_points = st.slider("Number of data points", 10, 100, 50)
    show_raw_data = st.checkbox("Show raw data")

# Main content area
if selected_option == "Overview":
    st.header("Overview")
    st.write("A summary of your data and key metrics.")

    # Create some dummy data
    data = pd.DataFrame(
        np.random.rand(data_points, 3),
        columns=['A', 'B', 'C']
    )

    # Display metrics in columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Items", data_points * 2)
    with col2:
        st.metric("Average Value", f"{data['A'].mean():.2f}")
    with col3:
        st.metric("Max Value", f"{data['B'].max():.2f}")

    st.subheader("Data Visualization")
    st.line_chart(data)

    if show_raw_data:
        st.subheader("Raw Data")
        st.dataframe(data)

elif selected_option == "Detailed Analysis":
    st.header("Detailed Analysis")
    st.write("Dive deeper into specific aspects of the data.")
    
    # Example of using tabs for different analysis views
    tab1, tab2 = st.tabs(["Chart View", "Table View"])
    with tab1:
        st.subheader("Interactive Chart")
        # More complex chart using st.altair_chart or st.plotly_chart could go here
        st.bar_chart(np.random.rand(10, 2), use_container_width=True)
    with tab2:
        st.subheader("Detailed Table")
        st.table(pd.DataFrame({'Product': ['A', 'B', 'C'], 'Sales': [100, 150, 75]}))

elif selected_option == "Settings":
    st.header("Settings")
    st.write("Configure application preferences.")
    user_name = st.text_input("Your Name", "Guest")
    st.success(f"Welcome, {user_name}!")
    st.button("Save Settings")

st.markdown("---")
st.caption("Made with ❤️ by Madhukesh .")