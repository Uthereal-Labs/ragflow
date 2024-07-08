from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

setup(
    name='ragflow',
    version='0.2',
    packages=find_packages(),
    # install_requires=parse_requirements('requirements_arm.txt'),
    author='Original Author',
    author_email='author@example.com',
    description='RAGFlow is an open-source RAG (Retrieval-Augmented Generation) engine.',
    url='https://github.com/infiniflow/ragflow',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)