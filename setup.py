from setuptools import setup, find_packages

setup(
    name='Astadeus',
    version='0.0.1',
    description='The Astadeus library',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'cohere',
        'smart-open',
        'jsonlines',
        'anthropic==0.2.10',
        'scikit-learn',
        'evaluate',
        'scipy',
        'pandas',
        'sqlitedict',
        'torch',
        'transformers',
        'accelerate',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
