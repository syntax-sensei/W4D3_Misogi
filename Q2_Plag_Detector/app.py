import streamlit as st
from utils.preprocessing import preprocess
from utils.similarity import compute_similarity_matrix, find_clones
from embeddings.sentence_transformer import STEmbedder
from embeddings.openai_embedder import OpenAIEmbedder
import pandas as pd

from dotenv import load_dotenv
load_dotenv()

st.set_page_config("Semantic Plagiarism Detector", layout="wide")
st.title("🧠 Semantic Plagiarism Detector")

# Text Inputs
st.subheader("Enter multiple texts:")
text_inputs = []
for i in range(5):
    text = st.text_area(f"Text {i+1}", key=f"text_{i}")
    if text.strip():
        text_inputs.append(preprocess(text))

if len(text_inputs) < 2:
    st.warning("Enter at least 2 texts to compare.")
    st.stop()

# Embedding Model Choice
model_option = st.selectbox("Select Embedding Model", ["SentenceTransformer", "OpenAI"])

# Load Model
if model_option == "SentenceTransformer":
    embedder = STEmbedder()
elif model_option == "OpenAI":
    embedder = OpenAIEmbedder()

# Embed and Compare
with st.spinner("Generating embeddings and computing similarities..."):
    embeddings = embedder.get_embeddings(text_inputs)
    sim_matrix = compute_similarity_matrix(embeddings)
    clones = find_clones(sim_matrix)

# Show Matrix
st.subheader("🔢 Similarity Matrix (%)")
df = pd.DataFrame(sim_matrix, columns=[f"T{i+1}" for i in range(len(text_inputs))],
                              index=[f"T{i+1}" for i in range(len(text_inputs))])
st.dataframe(df)

# Clone Highlighting
st.subheader("⚠️ Potential Clones (>{}%)".format(80))
if clones:
    for i, j, score in clones:
        st.write(f"🟠 Text {i+1} and Text {j+1}: **{score}%** similarity")
else:
    st.success("No clones detected based on the current threshold.")

# Comparison Report
st.markdown("---")
st.subheader("📘 How Embeddings Detect Semantic Similarity")
st.markdown("""
Embedding models convert texts into high-dimensional vectors capturing semantics.  
Cosine similarity is used to measure closeness of meaning rather than word overlap.

- Sentence Transformers use transformers trained to align similar meanings.
- OpenAI embeddings (like `text-embedding-3-small`) are tuned for semantic search.
- Higher similarity implies greater risk of paraphrased or copied content.

You can experiment with both models above and observe the matrix differences.
""")
