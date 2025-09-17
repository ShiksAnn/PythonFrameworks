import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.title("📊 CORD-19 Data Explorer")
st.write("A simple interactive app for exploring COVID-19 research papers.")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv", nrows=5000)
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
year_min, year_max = int(df['year'].min()), int(df['year'].max())
year_range = st.sidebar.slider("Select year range", year_min, year_max, (2020, 2021))

filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Display sample data
st.subheader("📄 Sample Papers")
st.dataframe(filtered[['title', 'publish_time', 'journal']].head(10))

# Visualization 1: Publications by Year
st.subheader("📈 Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# Visualization 2: Top Journals
st.subheader("🏛️ Top Journals")
top_journals = filtered['journal'].value_counts().head(10)
fig, ax = plt.subplots()
top_journals.plot(kind="bar", ax=ax)
ax.set_ylabel("Number of Papers")
st.pyplot(fig)
