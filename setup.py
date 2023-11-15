# setup.py

from setuptools import setup

setup(
    name='LlamaRAGVectorStores',
    version='0.1',
    packages=['LlamaRAGVectorStores'],
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
