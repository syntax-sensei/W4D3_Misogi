# Plagiarism Detector

A comprehensive plagiarism detection system that uses multiple embedding models to identify similarities between documents.

## Features

- **Multiple Embedding Models**: Support for both OpenAI embeddings and SentenceTransformers
- **Text Preprocessing**: Advanced text cleaning and deduplication
- **Similarity Analysis**: Cosine similarity calculations with detailed matrix analysis
- **Streamlit Interface**: User-friendly web application for easy interaction
- **Comprehensive Reports**: Detailed comparison insights and analysis

## Project Structure

```
plagiarism_detector/
│
├── app.py                         # Streamlit app entry point
├── embeddings/
│   ├── __init__.py
│   ├── openai_embedder.py         # OpenAI embedding logic
│   └── sentence_transformer.py    # SentenceTransformers logic
├── utils/
│   ├── __init__.py
│   ├── preprocessing.py           # Text cleaning, deduplication
│   └── similarity.py              # Cosine similarity + matrix
├── reports/
│   └── model_comparison.md        # Comparison insights
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd plagiarism_detector
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables (if using OpenAI):
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Usage

### Running the Streamlit App

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## Configuration

### OpenAI Configuration
- Set your OpenAI API key as an environment variable
- Configure model parameters in `embeddings/openai_embedder.py`

### SentenceTransformers Configuration
- Model selection and parameters in `embeddings/sentence_transformer.py`
- Default model: `all-MiniLM-L6-v2`

## API Reference

### Embeddings Module

#### OpenAIEmbedder
- `embed(text: str) -> List[float]`: Generate embeddings using OpenAI API
- `batch_embed(texts: List[str]) -> List[List[float]]`: Batch embedding generation

#### SentenceTransformerEmbedder
- `embed(text: str) -> List[float]`: Generate embeddings using SentenceTransformers
- `batch_embed(texts: List[str]) -> List[List[float]]`: Batch embedding generation

