from setuptools import find_packages,setup

def get_requirements():
    pymongo
    pandas

setup(
    name="sensor",
    version="0.0.1",
    author="yash",
    author_email="yashvij1996@gmail.com",
    packages=find_packages(),
    istall_requires = get_requirements(),
)