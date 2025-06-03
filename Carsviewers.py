import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set page title
st.title("Car MSRP by Drive Train")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("../Datasets/CARS.csv")

df = load_data()

# Show all unique car makes
st.subheader("Select Car Make")
car_makes = df['Make'].unique()
selected_make = st.selectbox("Choose a car Make", car_makes)

# Filter data by selected make
filtered_data = df[df['Make'] == selected_make]

# Plot
if not filtered_data.empty:
    st.subheader(f"Average MSRP by Drive Train for {selected_make}")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=filtered_data, x="DriveTrain", y="MSRP", estimator=np.mean, ax=ax)
    ax.set_xlabel("Drive Train")
    ax.set_ylabel("Average MSRP")
    ax.set_title(f"{selected_make} - MSRP by Drive Train")
    plt.xticks(rotation=45)
    st.pyplot(fig)
else:
    st.warning("No data available for the selected car make.")
