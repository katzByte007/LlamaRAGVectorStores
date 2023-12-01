# setup.py

from setuptools import setup
with open("README.md","r") as f:
    long_description= f.read
setup(
    name='LlamaRAGVectorStores',
    version='0.1',
    packages=['LlamaRAGVectorStores'],
    long_description=long_description,
    long_description_content_type= "text/markdown"
    install_requires=[
        'llama-index',
        'openai',
        'transformers',
        'accelerate',
        'optimum[exporters]',
        'InstructorEmbedding',
        'sentence_transformers',
        'pypdf',
        'chromadb',
        'pinecone-client',
        'pydantic==1.10.11'
    ],
    entry_points={
        'console_scripts': [
            'LlamaRAGVectorStores=LlamaRAGVectorStores.main:main',
        ],
    },
)
