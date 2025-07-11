from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain import hub
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
import os

EMBEDDINGS_MODEL_NAME = "bkai-foundation-models/vietnamese-bi-encoder"

def load_embeddings():
    return HuggingFaceEmbeddings(model_name=EMBEDDINGS_MODEL_NAME)
    
def process_pdf(tmp_file_path, embeddings=load_embeddings()):
    loader = PyPDFLoader(tmp_file_path)
    documents = loader.load()
    
    semantic_splitter = SemanticChunker(
        embeddings=embeddings,
        buffer_size=1,
        breakpoint_threshold_type="percentile", 
        breakpoint_threshold_amount=95,
        min_chunk_size=500,
        add_start_index=True
    )
    
    docs = semantic_splitter.split_documents(documents)
    vector_db = Chroma.from_documents(documents=docs, embedding=embeddings)
    retriever = vector_db.as_retriever()
    
    return retriever