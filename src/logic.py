# logic.py

from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores import ChromaVectorStore

# How to Persist: Saving to Disk
db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("DB_collection")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

storage_context = StorageContext.from_defaults(vector_store=vector_store)

service_context = ServiceContext.from_defaults(embed_model=embed_model,
                                               chunk_size=800,
                                               chunk_overlap=20)

index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, service_context=service_context
)

# Load from Disk
db2 = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db2.get_or_create_collection("DB_collection")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

index = VectorStoreIndex.from_vector_store(
    vector_store,
    service_context=service_context,
)

# Query Data
query_engine = index.as_query_engine()

response = query_engine.query("What are some of the main contributions of this new Orca model?")

display(Markdown(f"{response}"))
