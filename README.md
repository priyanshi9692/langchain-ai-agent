# 🍕 Restaurant Review Chatbot

An intelligent chatbot that answers questions about a pizza restaurant using customer reviews. Built with RAG (Retrieval-Augmented Generation) architecture, combining semantic search with AI-powered responses.

## 📋 Table of Contents
- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [How It Works](#how-it-works)

---

## 🎯 Overview

This application uses advanced AI techniques to provide intelligent answers about a restaurant based on real customer reviews. Instead of generic responses, the chatbot retrieves relevant reviews and uses them as context to generate accurate, grounded answers.

**Key Features:**
- 💬 Interactive chat interface (Streamlit UI)
- 🔍 Semantic search through customer reviews
- 🤖 AI-powered responses using local LLM
- 📊 Citation of relevant reviews for transparency
- 🏠 Runs completely locally (no API costs!)

---

## 🛠 Technologies Used

### **LangChain Framework**
LangChain is a framework for developing applications powered by language models. It provides:
- **Chains**: Connect multiple components (prompts, models, retrievers) into pipelines
- **Prompt Templates**: Structured ways to format inputs for language models
- **Retrievers**: Interface for fetching relevant documents from vector stores
- **Modular Design**: Easy integration of different LLMs and vector databases

**Why use it?** Simplifies building complex AI applications with pre-built components and standardized interfaces.

### **Ollama**
Ollama is a tool for running large language models (LLMs) locally on your machine.

**Benefits:**
- 🔒 **Privacy**: Your data never leaves your computer
- 💰 **Cost**: No API fees or usage limits
- ⚡ **Speed**: No network latency
- 🎯 **Control**: Choose from various open-source models (Llama, Mistral, etc.)

**In this project:** We use `llama3.2` for generating responses and `mxbai-embed-large` for creating embeddings.

### **ChromaDB**
Chroma is an open-source vector database designed for AI applications.

**What it does:**
- 📦 **Stores embeddings**: Numerical representations of text documents
- 🔎 **Semantic search**: Finds similar documents by meaning, not keywords
- 💾 **Persistence**: Saves your vector database to disk for reuse
- ⚡ **Performance**: Fast similarity search even with thousands of documents

**In this project:** Stores restaurant review embeddings and retrieves the most relevant reviews for each question.

---

## 📁 Project Structure

```
agentic-ai/
├── app.py                              # Streamlit web application
├── main.py                             # CLI version of the chatbot
├── vector.py                           # Vector store setup and retriever
├── realistic_restaurant_reviews.csv    # Customer reviews dataset
├── requirements.txt                    # Python dependencies
├── README.md                           # This file
└── chroma_langchain_db/               # ChromaDB storage (created on first run)
```

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8 or higher
- [Ollama](https://ollama.ai) installed on your system

### 1. Install Ollama and Download Models

First, install Ollama from [https://ollama.ai](https://ollama.ai)

Then download the required models:

```bash
# For chat/text generation
ollama pull llama3.2

# For creating embeddings
ollama pull mxbai-embed-large
```

Verify installation:
```bash
ollama list
```

### 2. Clone/Download the Project

```bash
cd /path/to/your/workspace
# If you have the project, navigate to it
cd agentic-ai
```

### 3. Create Python Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv myvenv
source myvenv/bin/activate
```

**On Windows:**
```bash
python -m venv myvenv
myvenv\Scripts\activate
```

You should see `(myvenv)` in your terminal prompt.

### 4. Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This will install:
- `langchain` - Core framework
- `langchain-ollama` - Ollama integration
- `langchain-chroma` - ChromaDB integration
- `pandas` - Data processing
- `streamlit` - Web interface

### 5. First-Time Setup (Vector Database)

On first run, the application will:
1. Read the CSV file with restaurant reviews
2. Create embeddings for each review
3. Store them in ChromaDB (in `chroma_langchain_db/` folder)

This only happens once. Subsequent runs will reuse the existing database.

---

## 🎮 Running the Application

### Option 1: Streamlit Web Interface (Recommended)

```bash
# Make sure your virtual environment is activated
source myvenv/bin/activate  # On macOS/Linux
# or
myvenv\Scripts\activate     # On Windows

# Run the Streamlit app
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

**Features:**
- Chat-style interface
- View relevant reviews used for each answer
- Clear conversation history
- Example questions in sidebar

### Option 2: Command Line Interface

```bash
# Make sure your virtual environment is activated
source myvenv/bin/activate  # On macOS/Linux
# or
myvenv\Scripts\activate     # On Windows

# Run the CLI version
python main.py
```

Type your questions and press Enter. Type `q` to quit.

---

## 🔍 How It Works

### RAG (Retrieval-Augmented Generation) Pipeline

1. **User asks a question**: "What do customers say about the pizza quality?"

2. **Question Embedding**: The question is converted to a vector using `mxbai-embed-large`

3. **Semantic Search**: ChromaDB finds the 5 most similar reviews based on vector similarity

4. **Context Construction**: Retrieved reviews are formatted into a prompt

5. **AI Generation**: Llama 3.2 generates an answer using the reviews as context

6. **Response**: User receives an accurate answer with optional review citations

### Example Flow

```
Question: "Is the delivery fast?"
    ↓
[Embedding Model] → Vector: [0.23, -0.45, 0.67, ...]
    ↓
[ChromaDB Search] → Top 5 relevant reviews about delivery
    ↓
[Prompt Template] → "You are an expert... Here are reviews: [reviews]... Question: [question]"
    ↓
[Llama 3.2] → "Based on customer reviews, delivery times are generally..."
```

---

## 💡 Example Questions to Ask

- What do customers say about the pizza quality?
- Is the service good at this restaurant?
- Are there any complaints about delivery?
- What's the best pizza to order?
- How's the atmosphere?
- Do customers recommend this place?

---

## 🔧 Troubleshooting

### "ModuleNotFoundError: No module named 'langchain_ollama'"
**Solution:** Make sure your virtual environment is activated and dependencies are installed:
```bash
source myvenv/bin/activate
pip install -r requirements.txt
```

### "Error connecting to Ollama"
**Solution:** Make sure Ollama is running and models are downloaded:
```bash
ollama list
ollama pull llama3.2
ollama pull mxbai-embed-large
```

### Slow first run
**Normal behavior!** Creating embeddings for all reviews takes time on the first run. Subsequent runs are much faster.

### ChromaDB not found
**Solution:** Delete the `chroma_langchain_db` folder and run again to recreate it:
```bash
rm -rf chroma_langchain_db
python app.py
```

---

## 📚 Learn More

- **LangChain Documentation**: [https://python.langchain.com](https://python.langchain.com)
- **Ollama Documentation**: [https://ollama.ai/docs](https://ollama.ai/docs)
- **ChromaDB Documentation**: [https://docs.trychroma.com](https://docs.trychroma.com)
- **Streamlit Documentation**: [https://docs.streamlit.io](https://docs.streamlit.io)

---

## 📝 Notes

- All processing happens locally on your machine
- No data is sent to external APIs
- The vector database persists between runs for faster startup
- You can add more reviews to the CSV file and delete the `chroma_langchain_db` folder to rebuild the database

---

## 🤝 Contributing

Feel free to fork this project and customize it for your own use cases:
- Replace the CSV file with your own data
- Change the prompt template for different use cases
- Try different Ollama models
- Customize the Streamlit UI

---

**Happy Chatting! 🍕✨**

