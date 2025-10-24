import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# Page configuration
st.set_page_config(
    page_title="Restaurant Review Chatbot",
    page_icon="🍕",
    layout="centered"
)

# Initialize the model and prompt
@st.cache_resource
def get_model():
    return OllamaLLM(model="llama3.2")

@st.cache_resource
def get_chain():
    model = get_model()
    template = """
You are an expert in answering questions about a pizza restaurant.

Here are some relevant reviews: {reviews}

Here is the question: {question}

"""
    prompt = ChatPromptTemplate.from_template(template)
    return prompt | model

chain = get_chain()

# App title and description
st.title("🍕 Restaurant Review Chatbot")
st.markdown("Ask me anything about our pizza restaurant based on customer reviews!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        # Show relevant reviews if available
        if message["role"] == "assistant" and "reviews" in message:
            with st.expander("📝 View relevant reviews used"):
                for i, doc in enumerate(message["reviews"], 1):
                    st.markdown(f"**Review {i}** (Rating: {doc.metadata.get('rating', 'N/A')})")
                    st.markdown(f"_{doc.page_content}_")
                    st.markdown("---")

# Chat input
if question := st.chat_input("Ask your question about the restaurant..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": question})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(question)
    
    # Get relevant reviews
    with st.spinner("Searching through reviews..."):
        reviews = retriever.invoke(question)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = chain.invoke({
                "reviews": reviews,
                "question": question
            })
        st.markdown(result)
        
        # Show relevant reviews in expander
        with st.expander("📝 View relevant reviews used"):
            for i, doc in enumerate(reviews, 1):
                st.markdown(f"**Review {i}** (Rating: {doc.metadata.get('rating', 'N/A')})")
                st.markdown(f"_{doc.page_content}_")
                st.markdown("---")
    
    # Add assistant response to chat history
    st.session_state.messages.append({
        "role": "assistant", 
        "content": result,
        "reviews": reviews
    })

# Sidebar with additional information
with st.sidebar:
    st.header("About")
    st.info(
        "This chatbot uses RAG (Retrieval-Augmented Generation) to answer "
        "questions about a pizza restaurant based on real customer reviews."
    )
    
    st.header("How it works")
    st.markdown("""
    1. **Ask a question** about the restaurant
    2. **Relevant reviews** are retrieved from the database
    3. **AI generates** an answer based on those reviews
    """)
    
    st.header("Examples")
    st.markdown("""
    - What do customers say about the pizza?
    - Is the service good?
    - What's the best pizza to order?
    - Are there any complaints about delivery?
    """)
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

