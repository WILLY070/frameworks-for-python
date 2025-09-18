import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 1. Load data
df = pd.read_csv("metadata.csv")

# 2. Clean data safely
df_clean = df.copy()

# Ensure 'title' column exists
if 'title' in df_clean.columns:
    df_clean['title'] = df_clean['title'].fillna("Untitled")
else:
    df_clean['title'] = "Untitled"

# Ensure 'abstract' column exists
if 'abstract' in df_clean.columns:
    df_clean['abstract'] = df_clean['abstract'].fillna("")
else:
    df_clean['abstract'] = ""  # create empty column

# Ensure 'journal' column exists
if 'journal' in df_clean.columns:
    df_clean['journal'] = df_clean['journal'].fillna("Unknown Journal")
else:
    df_clean['journal'] = "Unknown Journal"

# Ensure 'publish_time' column exists
if 'publish_time' in df_clean.columns:
    df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
else:
    df_clean['publish_time'] = pd.NaT

# 3. Continue with your analysis / Streamlit app below...
st.title("CORD-19 Metadata Explorer")

st.write("### Preview of cleaned data")
st.dataframe(df_clean.head())
