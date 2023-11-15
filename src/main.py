# main.py

from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext
from llama_index.embeddings import HuggingFaceEmbedding
from llama_index.llms import OpenAI
from IPython.display import Markdown, display
import chromadb

# Define embedding function
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

documents = SimpleDirectoryReader(
    input_files=["Orca_paper.pdf"]
).load_data()

# CHROMA-DB
chroma_client = chromadb.EphemeralClient()
chroma_collection = chroma_client.create_collection("orca_paper")

# Set up ChromaVectorStore and load in data
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

storage_context = StorageContext.from_defaults(vector_store=vector_store)

service_context = ServiceContext.from_defaults(embed_model=embed_model)

index = VectorStoreIndex.from_documents(documents,
                                        storage_context=storage_context,
                                        service_context=service_context)

# Query Data
query_engine = index.as_query_engine()

response = query_engine.query("What are some of the main contributions of this new Orca model?")

display(Markdown(f"{response}"))
