# setup.py

from setuptools import setup

setup(
    name='your_package_name',
    version='0.1',
    packages=['your_package_name'],
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
            'your_package_name=your_package_name.main:main',
        ],
    },
)
