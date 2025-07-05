# 📄 RAG Chunking Strategy Visualizer

A Streamlit-based interactive application for visualizing and comparing different text chunking strategies used in Retrieval-Augmented Generation (RAG) systems.

## 🚀 Features

- **PDF Document Upload**: Upload and extract text from PDF documents
- **Multiple Chunking Strategies**: Compare 5 different chunking approaches
- **Interactive Parameters**: Adjust chunk size and overlap settings
- **Real-time Visualization**: See chunks in a formatted table with statistics
- **Strategy Explanations**: Learn about each chunking method

## 🧩 Available Chunking Strategies

### 1. Fixed Size (Characters)
- Splits text into equal-sized character chunks
- Simple and fast but may break context
- Good for consistent chunk sizes

### 2. Fixed Size (Words)
- Splits text by word count
- Maintains better boundaries than character-based
- Preserves word integrity

### 3. Sentence Based
- Uses regex to split by sentence boundaries
- Groups sentences up to a word limit
- Maintains semantic coherence within sentences

### 4. Sliding Window with Overlap
- Creates overlapping chunks for better retrieval
- Maintains context across chunk boundaries
- Improves retrieval performance

### 5. Semantic Chunking
- Uses sentence embeddings to group similar sentences
- Creates semantically coherent chunks
- Based on meaning rather than arbitrary boundaries

## 📁 Project Structure

```
├── app.py                # Streamlit main application
├── chunking/             # Chunking strategy implementations
│   ├── __init__.py       # Package initialization
│   ├── fixed_size.py     # Fixed size chunking (characters/words)
│   ├── sentence_based.py # Sentence-based chunking
│   ├── sliding_window.py # Sliding window with overlap
│   └── semantic_chunking.py # Semantic chunking with embeddings
├── utils/                # Utility functions
│   ├── __init__.py       # Package initialization
│   ├── pdf_loader.py     # PDF text extraction
│   ├── explainers.py     # Strategy explanations
│   └── visualizer.py     # Chunk visualization
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Q3_RAG_Chunking
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501` (or the URL shown in terminal)


## 🎯 Usage

1. **Upload a PDF**: Use the file uploader to select a PDF document
2. **Choose Strategy**: Select from the 5 available chunking strategies
3. **Adjust Parameters**: Set chunk size and overlap as needed
4. **View Results**: See the generated chunks in the table below
5. **Compare**: Try different strategies on the same document

## 🔧 Configuration

### Chunk Size
- **Range**: 50-2000 words/characters
- **Default**: 500
- **Impact**: Larger chunks preserve more context, smaller chunks are more focused

### Overlap
- **Range**: 0-1000 words
- **Default**: 100
- **Impact**: Higher overlap improves retrieval but increases storage

## 🧠 How It Works

### Text Extraction
- Uses PyPDF2 to extract text from uploaded PDFs
- Handles multi-page documents
- Preserves text formatting

### Chunking Process
1. **Text Preprocessing**: Clean and normalize extracted text
2. **Strategy Application**: Apply selected chunking algorithm
3. **Chunk Generation**: Create chunks based on strategy rules
4. **Visualization**: Display chunks with metadata

### Semantic Chunking Details
- Uses `all-MiniLM-L6-v2` sentence transformer model
- Computes cosine similarity between sentences
- Groups sentences with similarity > 0.3
- Maintains maximum word limit per chunk

## 📊 Output Format

Each chunk is displayed with:
- **Chunk Index**: Sequential numbering
- **Preview**: First 100 characters with ellipsis
- **Length (chars)**: Character count
- **Word Count**: Word count

