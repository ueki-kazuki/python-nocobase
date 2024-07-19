from setuptools import setup, find_packages


setup(
   name='nocobase',
   version='0.0.10',
   author='Kazuki UEKI',
   author_email='ueki.kazuki@gmail.com',
   packages=find_packages(),
   license='MIT',
   url='https://github.com/ueki-kazuki/python-nocobase',
   classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
   ],
   description='A package to use NocoBase API in a simple way',
   long_description=open('README.md').read(),
   long_description_content_type="text/markdown",
   install_requires=[
       "requests>=2.0",
   ],
)
