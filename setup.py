from setuptools import setup, find_packages


setup(
    name='python-nocobase',
    version='0.0.16',
    author='Kazuki UEKI',
    author_email='ueki.kazuki@gmail.com',
    packages=find_packages(),
    license='MIT',
    url='https://github.com/ueki-kazuki/python-nocobase',
    project_urls={
        'Bug Reports': 'https://github.com/ueki-kazuki/python-nocobase/issues',
        'Source': 'https://github.com/ueki-kazuki/python-nocobase',
        'Documentation': 'https://github.com/ueki-kazuki/python-nocobase#readme',
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Database",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    description='A Python client library for NocoBase API - an Airtable alternative',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    keywords='nocobase api client database airtable',
    python_requires='>=3.7',
    install_requires=[
        "requests>=2.25.0",
    ],
)
