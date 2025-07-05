import streamlit as st
from utils.pdf_loader import extract_text_from_pdf
from utils.visualizer import display_chunks_table
from utils.explainers import explain_strategy
from chunking import fixed_size, sentence_based, sliding_window, semantic_chunking

# Title
st.set_page_config(layout="wide")
st.title("📄 RAG Chunking Strategy Visualizer")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF Document", type=["pdf"])

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    st.subheader("Extracted Text Preview")
    st.text_area("Text", text[:2000], height=200)

    # Select chunking strategy
    strategy = st.selectbox("Choose a Chunking Strategy", [
        "Fixed Size (Characters)",
        "Fixed Size (Words)",
        "Sentence Based",
        "Sliding Window with Overlap",
        "Semantic Chunking"
    ])

    # Explanation
    st.markdown("### 📘 Strategy Explanation")
    st.info(explain_strategy(strategy))

    # Parameters
    chunk_size = st.number_input("Chunk Size", min_value=50, max_value=2000, value=500)
    overlap = st.number_input("Overlap (if applicable)", min_value=0, max_value=1000, value=100)

    # Chunking
    st.markdown("### 🧩 Generated Chunks")
    if strategy == "Fixed Size (Characters)":
        chunks = fixed_size.chunk_by_chars(text, chunk_size)
    elif strategy == "Fixed Size (Words)":
        chunks = fixed_size.chunk_by_words(text, chunk_size)
    elif strategy == "Sentence Based":
        chunks = sentence_based.chunk_by_sentences(text, chunk_size)
    elif strategy == "Sliding Window with Overlap":
        chunks = sliding_window.chunk_with_overlap(text, chunk_size, overlap)
    elif strategy == "Semantic Chunking":
        chunks = semantic_chunking.semantic_chunk(text, chunk_size)

    display_chunks_table(chunks)