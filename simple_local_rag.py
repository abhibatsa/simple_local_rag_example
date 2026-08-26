import os
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_chroma import Chroma
from langchain_core.documents import Document

# 1. Initialize local models with memory management constraints
# keep_alive="0" unloads the model from RAM immediately after generating an answer
llm = OllamaLLM(
    model="llama3.2:1b", 
    client_kwargs={"timeout": 60.0},
    keep_alive="0" 
)

embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
    keep_alive="0"
)

# 2. Hardcoded internal database documents
raw_documents = [
    Document(page_content="The secret code to bypass the laboratory main door is 9942X."),
    Document(page_content="The laboratory cafeteria serves fresh pizza every Tuesday at 12:00 PM."),
    Document(page_content="Project Quantum-X was authorized by Director Sarah Jenkins in 2024.")
]

print(">>> Initializing local vector store and generating embeddings...")
# Create a local in-memory vector database
vector_store = Chroma.from_documents(raw_documents, embeddings)
# Configure retriever to fetch the top 2 most matching text chunks
retriever = vector_store.as_retriever(search_kwargs={"k": 2}) 

# 3. Simple, explicit prompt designed for small 1B/3B models
template = """Context information is below.
---------------------
{context}
---------------------
Given the context information above and not prior knowledge, answer the query.
Query: {question}
Answer:"""

prompt = PromptTemplate(input_variables=["context", "question"], template=template)

# 4. Pipeline Execution Logic
def run_rag_pipeline(query: str):
    # Fetch related text snippets from vector database
    retrieved_docs = retriever.invoke(query)
    
    # Fallback if the database found absolutely nothing close
    if not retrieved_docs:
        return "I cannot find any related context in my database to answer this."
        
    context_text = "\n".join([doc.page_content for doc in retrieved_docs])
    
    # Format and run payload through LLM
    formatted_prompt = prompt.format(context=context_text, question=query)
    return llm.invoke(formatted_prompt)

# 5. Interactive UI Loop
print("\n=== Local Interactive RAG Pipeline Active ===")
print("Type 'exit' or 'quit' to terminate the session.\n")

while True:
    user_question = input("User Question: ")
    
    if user_question.lower() in ['exit', 'quit', 'q']:
        print("Shutting down pipeline. Goodbye!")
        break
        
    if not user_question.strip():
        continue
        
    try:
        print("Searching database & generating answer...")
        answer = run_rag_pipeline(user_question)
        print(f"AI Answer: {answer}\n")
    except Exception as e:
        print(f"Pipeline Error: {e}\n")

