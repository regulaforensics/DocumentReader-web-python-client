# coding: utf-8
import os

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="regula.documentreader.webclient",
    version=os.getenv("PACKAGE_VERSION_TO_PUBLISH", "7.4.45"),
    python_requires=">=3.8",
    description="Regula's Document Reader python client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Regula Forensics, Inc.",
    author_email="support@regulaforensics.com",
    url="https://regulaforensics.com",
    keywords=[
        "document-reader-client",
        "document reader",
        "document recognition",
        "regulaforensics",
        "regula",
    ],
    install_requires=[
        "certifi>=2024.07.04",
        "six>=1.10",
        "python-dateutil>=2.5.3",
        "urllib3>=1.26.19",
        "vistir>=0.4.0, <=0.6.1",
        "idna==3.7",
        "requests>=2.32.3",
    ],
    packages=find_packages(exclude=["test", "tests", "example"]),
    include_package_data=True,
)
