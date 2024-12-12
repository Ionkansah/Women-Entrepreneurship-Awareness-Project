import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Title of the Streamlit App
st.title("Entrepreneurship Among Women in Sunyani")

# Load the dataset
@st.cache_data
def load_data():
    # Adjust this path if the dataset is stored elsewhere
    return pd.read_csv("WOMEN_AWARENESS_PROJECT/data/AGE-CHILDREN-Map_cleaned_data.csv")

# Load and display the data
data = load_data()
st.write("### Dataset Overview")
st.dataframe(data)

# Display statistics
st.write("### Summary Statistics")
st.write(data.describe())

# Interactive Filter
st.write("### Filter Data by Age")
age_filter = st.slider("Select Age Range:", int(data["AGE"].min()), int(data["AGE"].max()), (20, 40))
filtered_data = data[(data["AGE"] >= age_filter[0]) & (data["AGE"] <= age_filter[1])]
st.write(f"Showing data for ages {age_filter[0]} to {age_filter[1]}:")
st.dataframe(filtered_data)

# Visualizations
st.write("### Data Visualization")
if st.checkbox("Show Correlation Heatmap"):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots()
    sns.heatmap(data.corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)
    
# Bar Chart
st.subheader("Marital Status Distribution")
marital_status_counts = data['MARITAL STATUS'].value_counts()
st.bar_chart(marital_status_counts)

# Pie Chart (using Plotly)
import plotly.express as px
st.subheader("Educational Background Distribution")
fig = px.pie(data, names='EDUCATIONAL BACKGROUND', title="Educational Background Distribution")
st.plotly_chart(fig)

# Success score display
st.write("### Business Success Rating Analysis")
st.bar_chart(data["HOW WILL YOU RATE YOUR BUSINESS SUCCESS ON A SCALE OF 10?"].value_counts())

# Footer
st.write("Developed with ❤️ by ISAAC OPOKU NKANSAH (ION) as a beta app")
