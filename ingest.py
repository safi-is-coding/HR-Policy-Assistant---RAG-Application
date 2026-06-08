from dotenv import load_dotenv
load_dotenv()

from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_chroma import Chroma

def load_documents(data_path):
    docs = []

    for pdf in Path(data_path).glob("*.pdf"):

        loader = PyPDFLoader(str(pdf))

        pdf_docs = loader.load()

        for doc in pdf_docs:
            doc.metadata["source_file"] = pdf.name

        docs.extend(pdf_docs)
    
    print(f"Loaded {len(docs)} pages")
    

    return docs


DATA_PATH = "data"
DB_PATH = "vector_db"

docs = load_documents(DATA_PATH)

# for pdf in Path(DATA_PATH).glob("*.pdf"):
    
#     loader = PyPDFLoader(str(pdf))
#     docs = loader.load()
    
#     for doc in docs:
#         doc.metadata["source_file"] = pdf.name
        
#     all_docs.extend(docs)
    

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)

chunks = splitter.split_documents(docs)

print(f"Created {len(chunks)} chunks")

embedding_model = MistralAIEmbeddings()


vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory=DB_PATH
)

print("Vector database created successfully")

