import streamlit as st
import pandas as pd

def display_chunks_table(chunks):
    data = [{
        "Chunk Index": i,
        "Preview": chunk[:100] + ("..." if len(chunk) > 100 else ""),
        "Length (chars)": len(chunk),
        "Word Count": len(chunk.split())
    } for i, chunk in enumerate(chunks)]

    df = pd.DataFrame(data)
    st.dataframe(df)