import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='Mits_AI_Dreamers',
    version='2024.0.1',
    author='Madhu Praneeth Lokesh',
    author_email='lokeshreddy2680@gmail.com',
    description='A package for computing Hamming distance, Jaccard coefficient, and overlap.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),  # Ensures it finds all sub-packages
    url='https://github.com/madhukm2050/Mits_AI_Dreamers',
    license='GPLv3',
    install_requires=[
        'psutil',
        'pandas',
        'plotly',
        'matplotlib',
        'validators',
        'urllib3',
        'Pillow',
        'numpy',
        'sphinx',
        'sphinx-rtd-theme',
        'discord.py',
        'networkx',
        'deprecated',
    ],
    extras_require={
        'gpu': ['cupy', 'pycuda'],
        'spark': ['pyspark'],
        'dev': ['twine', 'setuptools', 'build'],
        'all': ['cupy', 'pycuda', 'pyspark', 'twine', 'setuptools', 'build']
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
